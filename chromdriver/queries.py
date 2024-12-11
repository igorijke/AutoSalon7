from sqlalchemy import func
from chromdriver.models import Automobile, Order

def join_query(db):
    result = db.query(Automobile.brand, Automobile.model, Order.order_date).join(Order, Automobile.id == Order.automobile_id).all()
    return result

def filter_query(db, price_threshold):
    return db.query(Automobile).filter(Automobile.price > price_threshold).all()

def aggregate_query(db):
    return db.query(func.avg(Automobile.price).label("average_price")).scalar()
