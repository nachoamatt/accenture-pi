from db.connector import DatabaseConnector

def test_connection():
    try:
        conn = DatabaseConnector()
        engine = conn.engine
        assert engine is not None
        print("✅ Conexión a la base de datos establecida correctamente")
    except Exception as e:
        print("❌ Error al conectar a la base de datos:")
        print(e)

if __name__ == "__main__":
    test_connection()
