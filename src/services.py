"""Business logic."""
from typing import List
from interfaces import UserStatus, IUser, IRecipe, IItem, RecipeStatus
from io import BytesIO
from datetime import datetime
import uuid


class ServiceError(Exception):
    pass


class RecipeService(object):
    """Encapsulates business logic and db integration."""

    @classmethod
    async def create(cls, user_id: str, recipe: BytesIO) -> IRecipe:
        # 1. Load document
        # 2. Make OCR
        # 3. Post-process text: recognize structure.
        # 4. Put in db
        return IRecipe(
            recipe_id=str(uuid.uuid4()), 
            overall=2, 
            items=IItem(item_id=1, recipe_id=str(uuid.uuid4()), name="Sample"), 
            user_id=user_id, 
            raw_image_path="aboba", 
            created_at=datetime.now(), 
            updated_at=datetime.now(), 
            status=RecipeStatus.Processed,
        )

    @classmethod
    async def update_status(cls, user_id: str, recipe_id: str, recipe_status: RecipeStatus) -> IRecipe:
        # get Recipe by user & recipe_id...
        # UPDATE recipe.is_approved WHERE user_id = % AND recipe.id = $
        return IRecipe(
            recipe_id=str(uuid.uuid4()), 
            overall=2, 
            items=IItem(item_id=1, recipe_id=str(uuid.uuid4()), name="Sample"), 
            user_id=user_id, 
            raw_image_path="aboba", 
            created_at=datetime.now(),
            updated_at=datetime.now(), 
            status=recipe_status,
        )
    
    @classmethod
    async def discard(cls, user_id: str, recipe_id: str) -> IRecipe:
        return IRecipe(
            recipe_id=recipe_id, 
            overall=2, 
            items=IItem(item_id=1, recipe_id=recipe_id, name="Sample"), 
            user_id=user_id, 
            raw_image_path="aboba", 
            created_at=datetime.now(), 
            updated_at=datetime.now(), 
            status=RecipeStatus.Discarded,
        )

    @classmethod
    async def update(cls, user_id: str, recipe_updated: IRecipe) -> IRecipe:
        return IRecipe(
            recipe_id=1, 
            overall=2, 
            items=IItem(item_id=1, recipe_id=1, name="Sample"), 
            user_id=user_id, 
            raw_image_path="aboba", 
            created_at=datetime.now(), 
            updated_at=datetime.now(), 
            status=RecipeStatus.Discarded,
        )

    @classmethod
    async def statistics(cls):
        pass

    @classmethod
    async def get_all(cls, page: int) -> List[IRecipe]:
        pass
    

class UserService(object):
    @classmethod
    async def activate_user(cls, passphrase: str, chat_id: int) -> UserStatus:
        return UserStatus.Active
    
    @classmethod
    async def get_by_tg_id(cls, tg_id: int) -> IUser:
        return IUser(
            user_id=1,
            tg_id=tg_id,
            status=UserStatus.Active
        )
