from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import used_promotion as controller
from ..schemas import used_promotion as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['UsedPromotions'],
    prefix="/used_promotions"
)


@router.post("/", response_model=schema.UsedPromotion)
def create(request: schema.UsedPromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.UsedPromotion])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.UsedPromotion)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.UsedPromotion)
def update(item_id: int, request: schema.UsedPromotionUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
