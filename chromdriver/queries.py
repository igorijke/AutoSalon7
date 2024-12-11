def filter_query(cursor, price_threshold):
    cursor.execute("SELECT * FROM Automobiles WHERE Price > ?", (price_threshold,))
    return cursor.fetchall()

def aggregate_query(cursor):
    cursor.execute("SELECT AVG(Price) as AveragePrice FROM Automobiles")
    row = cursor.fetchone()
    return row.AveragePrice
