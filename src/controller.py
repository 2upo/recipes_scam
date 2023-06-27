import json
import logging
from utils import is_valid_uuid

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler
from telegram.ext.filters import PHOTO
from services import RecipeService, UserService
from interfaces import UserStatus, IUser, IRecipe, RecipeStatus
from functools import wraps
from io import BytesIO
from config import Config


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def require_auth(function):
    """Check if user is activated (went through auth flow)."""
    @wraps(function)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        """Wrap async protected handler call."""
        tg_user_id = (update.message or update.callback_query).from_user.id
        user = await UserService.get_by_tg_id(tg_user_id)
        if user.status == UserStatus.Active:
            return await function(update, context, user=user, *args, **kwargs)
        else:
            await update.message.reply_text("aboba")
    return wrapper


@require_auth
async def handle_recipe(update: Update, context: ContextTypes.DEFAULT_TYPE, user: IUser = None) -> None:
    """Send welcome message."""
    file = await update.message.photo[-1].get_file()
    
    file_buff = BytesIO()
    await file.download_to_memory(file_buff)

    recipe = await RecipeService.create(user_id=user.user_id, recipe=file_buff)
    callback_template = lambda recipe_id, new_status: json.dumps({
        "r": recipe_id, # recipe id
        "a": new_status.value, # action
    })

    keyboard = [
        [
            InlineKeyboardButton(
                "Confirm", 
                callback_data=callback_template(recipe.recipe_id, RecipeStatus.Confirmed),
            ),
        ],        
        [
            InlineKeyboardButton(
                "Discard", 
                callback_data=callback_template(recipe.recipe_id, RecipeStatus.Discarded),
            ),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Kudos, {}. Ave to me, aboba!".format(
        update.message.from_user.full_name
    ) + str(recipe), reply_markup=reply_markup)


@require_auth
async def handle_action(update: Update, context: ContextTypes.DEFAULT_TYPE, user: IUser = None) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()
    try:
        user_action = json.loads(query.data)
        recipe_id = user_action["r"]
        new_status = RecipeStatus(user_action["a"])
        if not is_valid_uuid(recipe_id):
            raise Exception("Passed invalid UUID")
        updated_recipe = await RecipeService.update_status(
            user_id=user.user_id,
            recipe_id=recipe_id,
            recipe_status=new_status,
        )
    except:
        query.edit_message_text(text="Something went wrong. Please try again.")
    await query.edit_message_text(text=f"Updated recipe: {updated_recipe}")


def main() -> None:
    """Run the bot."""

    application = Application.builder().token(Config.TG_BOT_TOKEN).build()


    application.add_handler(CallbackQueryHandler(handle_action))
    application.add_handler(MessageHandler(filters=PHOTO, callback=handle_recipe))


    # Run the bot until the user presses Ctrl-C

    application.run_polling()
