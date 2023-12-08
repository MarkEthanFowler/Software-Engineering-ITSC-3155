from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import order_item as model
from ..models import dish as dish_model
from ..models import dish_ingredient as dish_ingredient_model
from ..models import feedback as feedback_model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.OrderItem(
        order_id=request.order_id,
        dish_id=request.dish_id
    )

    try:
        db.add(new_item)
        
        dish = db.query(dish_model.Dish).filter(dish_model.Dish.id == request.dish_id).first()
        for ingredient in dish.ingredients:
            ingredient = db.query(dish_ingredient_model.DishIngredient).filter(dish_ingredient_model.DishIngredient.id == ingredient.id)
            if ingredient.first().quantity - ingredient.first().serving_size < 0:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough ingredients!")
            ingredient.update({"quantity": ingredient.first().quantity - ingredient.first().serving_size}, synchronize_session=False)
        
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.OrderItem).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.OrderItem).filter(model.OrderItem.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.OrderItem).filter(model.OrderItem.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.OrderItem).filter(model.OrderItem.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def get_items_with_rating(db: Session, rating: int):
    try:
        result = db.query(model.OrderItem).join(feedback_model.Feedback).filter(feedback_model.Feedback.rating == rating).all()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result