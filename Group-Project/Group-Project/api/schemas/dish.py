from typing import Optional
from pydantic import BaseModel
from .dish_ingredient import DishIngredient

class DishBase(BaseModel):
    name: str
    description: str
    price: float
    calories: int
    category: str
    
class DishCreate(DishBase):
    pass


class DishUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    category: Optional[str] = None


class Dish(DishBase):
    id: int
    ingredients: list[DishIngredient]    
    class ConfigDict:
        from_attributes = True
