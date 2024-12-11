from chromdriver.db_util import get_connection
from chromdriver.crud import create_table, create_orders_table, insert_data, insert_order, read_data, read_orders, filter_query, join_query
from chromdriver.queries import aggregate_query

def menu(cursor):
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
            rows = read_data(cursor)
            for row in rows:
                print(row)
        elif choice == "2":
            brand = input("Введіть марку авто: ")
            model = input("Введіть модель авто: ")
            price = float(input("Введіть ціну авто: "))
            insert_data(cursor, brand, model, price)
        elif choice == "3":
            threshold = float(input("Введіть поріг ціни: "))
            filter_query(cursor, threshold)
        elif choice == "4":
            aggregate_query(cursor)
        elif choice == "5":
            automobile_id = int(input("Введіть ID автомобіля: "))
            order_date = input("Введіть дату замовлення (YYYY-MM-DD): ")
            insert_order(cursor, automobile_id, order_date)
        elif choice == "6":
            orders = read_orders(cursor)
            for order in orders:
                print(order)
        elif choice == "7":
            join_query(cursor)
        elif choice == "0":
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Створення таблиць, якщо вони ще не створені
        create_table(cursor)
        create_orders_table(cursor)

        # Запуск меню
        menu(cursor)

        # Закриття підключення
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"An error occurred: {e}")
