from src.db.connector import DatabaseConnector

def test_connection():
    try:
        conn = DatabaseConnector()
        engine = conn.engine
        assert engine is not None
        print("✅ test_connection pasó correctamente. Conexión establecida.")
    except Exception as e:
        print("❌ test_connection falló al intentar conectar a la base de datos:")
        print(e)
