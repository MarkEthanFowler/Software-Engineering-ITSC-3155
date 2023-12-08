from sqlalchemy import Column, ForeignKey, Integer
from ..dependencies.database import Base
from sqlalchemy.orm import relationship


class UsedPromotion(Base):
    __tablename__ = "used_promotion"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    promotion_id = Column(Integer, ForeignKey("promotion.id"), nullable=False)
    
    promotion = relationship("Promotion", backref="UsedPromotion", uselist=False)
