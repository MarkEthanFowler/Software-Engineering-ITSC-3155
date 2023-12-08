from . import (dish, orders, dish_ingredients, feedback, order_items, promotion, used_promotion)


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(dish_ingredients.router)
    app.include_router(dish.router)
    app.include_router(feedback.router)
    app.include_router(order_items.router)
    app.include_router(promotion.router)
    app.include_router(used_promotion.router)
