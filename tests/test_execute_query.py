from src.db.connector import DatabaseConnector
import pandas as pd

def test_execute_query():
    db = DatabaseConnector()
    query = "SELECT COUNT(*) AS total FROM customers;"  
    result = db.execute_query(query)

    assert isinstance(result, pd.DataFrame), "El resultado no es un DataFrame"
    assert "total" in result.columns, "La columna 'total' no está en el resultado"
    assert result.shape[0] == 1, "Se esperaba un único resultado"
