from chromdriver.models import Automobile, Order


def create_automobile(db, brand, model, price):
    auto = Automobile(brand=brand, model=model, price=price)
    db.add(auto)
    db.commit()
    db.refresh(auto)
    return auto

def read_automobiles(db):
    return db.query(Automobile).all()

def create_order(db, automobile_id, order_date):
    order = Order(automobile_id=automobile_id, order_date=order_date)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def read_orders(db):
    return db.query(Order).all()
