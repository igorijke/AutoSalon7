from chromdriver.db import get_db, engine
from chromdriver.models import Base
from chromdriver.crud import create_automobile, read_automobiles, create_order, read_orders
from chromdriver.queries import join_query, filter_query, aggregate_query

Base.metadata.create_all(bind=engine)

def menu():
    db = next(get_db())
    while True:
        print("\n1. Показати всі авто")
        print("2. Додати авто")
        print("3. Вибрати авто дорожчі за ціну")
        print("4. Порахувати середню ціну авто")
        print("5. Додати замовлення")
        print("6. Показати всі замовлення")
        print("7. Об'єднання таблиць (авто та замовлення)")
        print("0. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            autos = read_automobiles(db)
            for auto in autos:
                print(auto.id, auto.brand, auto.model, auto.price)
        elif choice == "2":
            brand = input("Введіть марку авто: ")
            model = input("Введіть модель авто: ")
            price = float(input("Введіть ціну авто: "))
            create_automobile(db, brand, model, price)
        elif choice == "3":
            threshold = float(input("Введіть поріг ціни: "))
            autos = filter_query(db, threshold)
            for auto in autos:
                print(auto.id, auto.brand, auto.model, auto.price)
        elif choice == "4":
            avg_price = aggregate_query(db)
            print(f"Середня ціна авто: {avg_price}")
        elif choice == "5":
            automobile_id = int(input("Введіть ID автомобіля: "))
            order_date = input("Введіть дату замовлення (YYYY-MM-DD): ")
            create_order(db, automobile_id, order_date)
        elif choice == "6":
            orders = read_orders(db)
            for order in orders:
                print(order.id, order.automobile_id, order.order_date)
        elif choice == "7":
            results = join_query(db)
            for result in results:
                print(result)
        elif choice == "0":
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    menu()
