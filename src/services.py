"""Business logic."""
from typing import List
from interfaces import UserStatus, IUser, IRecipe
from io import BytesIO


class ServiceError(Exception):
    pass


class RecipeService(object):
    """Encapsulates business logic and db integration."""

    @classmethod
    def create(cls, user_id: str, recipe: BytesIO) -> IRecipe:
        # 1. Load document
        # 2. Make OCR
        # 3. Post-process text: recognize structure.
        # 4. Put in db
        pass

    @classmethod
    def confirm(cls, user_id: str, recipe_id: str) -> IRecipe:
        # get use
        # get Recipe by user & recipe_id...
        # UPDATE recipe.is_approved WHERE user_id = % AND recipe.id = $
        pass
    
    @classmethod
    def discard(cls, user_id: str, recipe_id: str) -> IRecipe:
        pass

    @classmethod
    def update(cls, user_id: str, recipe_updated: IRecipe) -> IRecipe:
        pass

    @classmethod
    def statistics(cls):
        pass

    @classmethod
    def get_all(cls, page: int) -> List[IRecipe]:
        pass
    

class UserService(object):
    @classmethod
    def activate_user(cls, passphrase: str, chat_id: int) -> UserStatus:
        pass
    
    @classmethod
    def get_user_by_chat_id(cls, chat_id: int) -> IUser:
        pass