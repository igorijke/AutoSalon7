def create_table(cursor):
    """
    Створює таблицю Automobiles.
    """
    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Automobiles' AND xtype='U')
        CREATE TABLE Automobiles (
            ID INT PRIMARY KEY IDENTITY(1,1),
            Brand NVARCHAR(50),
            Model NVARCHAR(50),
            Price FLOAT
        )
    """)
    cursor.connection.commit()
    print("Table 'Automobiles' created successfully!")

def create_orders_table(cursor):
    """
    Створює таблицю Orders.
    """
    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Orders' AND xtype='U')
        CREATE TABLE Orders (
            OrderID INT PRIMARY KEY IDENTITY(1,1),
            AutomobileID INT FOREIGN KEY REFERENCES Automobiles(ID),
            OrderDate DATE
        )
    """)
    cursor.connection.commit()
    print("Table 'Orders' created successfully!")

def insert_data(cursor, brand, model, price):
    """
    Додає запис до таблиці Automobiles.
    :param cursor: об'єкт курсора
    :param brand: марка авто
    :param model: модель авто
    :param price: ціна авто
    """
    cursor.execute("INSERT INTO Automobiles (Brand, Model, Price) VALUES (?, ?, ?)", (brand, model, price))
    cursor.connection.commit()
    print(f"Inserted {brand} {model} with price {price}")

def insert_order(cursor, automobile_id, order_date):
    """
    Додає запис до таблиці Orders.
    :param cursor: об'єкт курсора
    :param automobile_id: ID автомобіля
    :param order_date: Дата замовлення
    """
    cursor.execute("INSERT INTO Orders (AutomobileID, OrderDate) VALUES (?, ?)", (automobile_id, order_date))
    cursor.connection.commit()
    print(f"Inserted order for AutomobileID {automobile_id} with date {order_date}")

def read_data(cursor):
    """
    Повертає всі записи з таблиці Automobiles.
    """
    cursor.execute("SELECT * FROM Automobiles")
    return cursor.fetchall()

def read_orders(cursor):
    """
    Повертає всі записи з таблиці Orders.
    """
    cursor.execute("SELECT * FROM Orders")
    return cursor.fetchall()

def join_query(cursor):
    """
    Виконує запит із об'єднанням таблиць Automobiles та Orders.
    """
    cursor.execute("""
        SELECT a.ID, a.Brand, a.Model, a.Price, o.OrderID, o.OrderDate
        FROM Automobiles a
        INNER JOIN Orders o ON a.ID = o.AutomobileID
    """)
    rows = cursor.fetchall()
    if rows:
        print("Об'єднані дані з таблиць Automobiles та Orders:")
        for row in rows:
            print(row)
    else:
        print("Жодного запису не знайдено в об'єднаних таблицях.")

def filter_query(cursor, price_threshold):
    """
    Вибирає авто дорожчі за вказану ціну.
    :param cursor: об'єкт курсора
    :param price_threshold: мінімальна ціна
    """
    cursor.execute("SELECT * FROM Automobiles WHERE Price > ?", (price_threshold,))
    rows = cursor.fetchall()
    if rows:
        print("Авто дорожчі за вказану ціну:")
        for row in rows:
            print(row)
    else:
        print(f"Жодне авто не дорожче за {price_threshold}.")
