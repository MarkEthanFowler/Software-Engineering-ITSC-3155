from typing import Optional
from pydantic import BaseModel


class FeedbackBase(BaseModel):
    order_item_id: int
    rating: int
    comments: str


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackUpdate(BaseModel):
    order_item_id: Optional[int] = None
    rating: Optional[int] = None
    comments: Optional[str] = None

class Feedback(FeedbackBase):
    id: int

    class ConfigDict:
        from_attributes = True