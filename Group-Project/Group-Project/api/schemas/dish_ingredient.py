from typing import Optional
from pydantic import BaseModel

class DishIngredientBase(BaseModel):
    name: str
    description: str
    serving_size: int
    quantity: int
    dish_id: int


class DishIngredientCreate(DishIngredientBase):
    pass


class DishIngredientUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    serving_size: Optional[int] = None
    quantity: Optional[int] = None
    dish_id: Optional[int] = None


class DishIngredient(DishIngredientBase):
    id: int

    class ConfigDict:
        from_attributes = True