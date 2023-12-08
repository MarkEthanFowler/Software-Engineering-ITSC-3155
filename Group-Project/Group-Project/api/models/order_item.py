from sqlalchemy import Column, ForeignKey, Integer
from ..dependencies.database import Base
from sqlalchemy.orm import relationship


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    dish_id = Column(Integer, ForeignKey("dishes.id"), nullable=False)
    
    dish = relationship("Dish", backref="OrderItem", uselist=False)
    feedback = relationship("Feedback", backref="OrderItem", uselist=False)
