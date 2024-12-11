import pyodbc

def get_connection():
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost,1433;"
        "DATABASE=AutoSalon;"
        "UID=sa;"
        "PWD=ogorer61;"
    )
    return pyodbc.connect(connection_string)
