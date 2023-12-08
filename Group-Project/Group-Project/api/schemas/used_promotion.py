from typing import Optional
from pydantic import BaseModel
from .promotion import Promotion

class UsedPromotionBase(BaseModel):
    order_id: int
    promotion_id: int
    pass


class UsedPromotionCreate(UsedPromotionBase):
    pass

class UsedPromotionUpdate(BaseModel):
    order_id: Optional[int] = None
    promotion_id: Optional[int] = None

class UsedPromotion(UsedPromotionBase):
    id: int

    promotion: Promotion

    class ConfigDict:
        from_attributes = True