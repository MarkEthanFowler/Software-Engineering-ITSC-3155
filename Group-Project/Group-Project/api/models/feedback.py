from sqlalchemy import Column, ForeignKey, Integer, String
from ..dependencies.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    order_item_id = Column(Integer, ForeignKey("order_items.id"), nullable=False)
    rating = Column(Integer)
    comments = Column(String(255))
