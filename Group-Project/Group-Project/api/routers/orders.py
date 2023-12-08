from datetime import date
from datetime import datetime
from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import order as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)

@router.get("/status/{item_id}", response_model=dict[str, str])
def get_status(item_id: int, db: Session = Depends(get_db)):
    return {
        'status': controller.read_one(db, item_id).status
    }
    
@router.get("/between_dates", response_model=list[schema.Order])
def read_between_dates(start_date: str, end_date: str, db: Session = Depends(get_db)):
    return controller.read_between_dates(db, start_date, end_date)

@router.get("/day_report", response_model=dict[str, int])
def get_day_report(day: date = date.today(), db: Session = Depends(get_db)):
    day_start = datetime.combine(day, datetime.min.time())
    day_end = datetime.combine(day, datetime.max.time())
    orders = controller.read_between_dates(db, day_start, day_end)
    total = (sum([order.total for order in orders]))
    return {
        'total': total,
        'numberOfOrders': len(orders)
    }

@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Order)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
