from sqlalchemy import Column, ForeignKey, Integer, String
from ..dependencies.database import Base


class DishIngredient(Base):
    __tablename__ = "dish_ingredients"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    name = Column(String(255))
    description = Column(String(255))
    serving_size = Column(Integer)
    quantity = Column(Integer)
    
    dish_id = Column(Integer, ForeignKey("dishes.id"), nullable=False)
