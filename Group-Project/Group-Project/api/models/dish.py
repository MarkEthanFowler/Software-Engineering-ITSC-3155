from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base
from sqlalchemy.orm import relationship


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(DECIMAL(4, 2))
    calories = Column(Integer)
    category = Column(String(255))
    
    ingredients = relationship("DishIngredient", backref="Dish")