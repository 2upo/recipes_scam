from dataclasses import dataclass, asdict
from collections import namedtuple
from enum import Enum
from io import BytesIO
from datetime import datetime
from typing import Optional, List

IUser = namedtuple("IUser", ["user_id", "chat_id", "is_active"])

UserStatus = Enum("UserStatus", ["Active", "Inactive", "Banned"])
RecipeStatus = Enum("UserStatus", ["Uploaded", "Processed", "Confirmed"])


@dataclass
class IItems(object):
    item_id: str
    recipe_id: str
    name: str = None
    name_translated: str = None
    price: int = None


@dataclass
class IRecipeContent():
    recipe_id: str
    overall: Optional[int] = None
    items: List[IItems] = []


@dataclass
class IRecipe(IRecipeContent):
    """Describes one recipe with it's content."""
    user_id: str
    raw_image_path: str
    created_at: datetime
    updated_at: datetime
    status: RecipeStatus = RecipeStatus.Uploaded
