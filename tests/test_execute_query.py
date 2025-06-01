from src.db.connector import DatabaseConnector
import pandas as pd

def test_execute_query():
    db = DatabaseConnector()
    query = "SELECT COUNT(*) AS total FROM customers;"
    result = db.execute_query(query)
    
    # Verificamos que es un DataFrame
    assert isinstance(result, pd.DataFrame)
    
    # Verificamos que tenga al menos una fila y la columna 'total'
    assert not result.empty
    assert 'total' in result.columns

    # Mostramos el resultado por consola (opcional)
    print(result)
