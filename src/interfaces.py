from dataclasses import dataclass, asdict, field
from collections import namedtuple
from enum import Enum
from io import BytesIO
from datetime import datetime
from typing import Optional, List

IUser = namedtuple("IUser", ["user_id", "tg_id", "status"])

UserStatus = Enum("UserStatus", ["Active", "Inactive", "Banned"])
RecipeStatus = Enum("RecipeStatus", ["Uploaded", "Processed", "Confirmed", "Discarded"])


@dataclass
class IItem(object):
    item_id: str
    recipe_id: str
    name: str = field(default=None)
    name_translated: str = field(default=None)
    price: int = field(default=None)


@dataclass
class IRecipeContent():
    recipe_id: str
    overall: Optional[int]
    items: List[IItem]


@dataclass
class IRecipe(IRecipeContent):
    """Describes one recipe with it's content."""
    user_id: str
    raw_image_path: str
    created_at: datetime
    updated_at: datetime
    status: RecipeStatus = field(default=RecipeStatus.Uploaded)
