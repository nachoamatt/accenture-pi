from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from dotenv import load_dotenv
import pandas as pd
import os

class DatabaseConnector:
    _instance = None
    _engine: Engine = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnector, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        load_dotenv()

        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD", "")  # Puede estar vacío
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "3306")
        database = os.getenv("DB_NAME")

        if not all([user, database]):
            raise ValueError("Faltan variables necesarias en el archivo .env")

        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self._engine = create_engine(url)

    @property
    def engine(self) -> Engine:
        return self._engine

    def execute_query(self, sql: str) -> pd.DataFrame:
        """Ejecuta una consulta SQL y devuelve los resultados en un DataFrame de pandas."""
        with self._engine.connect() as connection:
            result = connection.execute(text(sql))
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df

    def test_connection(self) -> bool:
        """Intenta ejecutar una consulta de prueba para validar la conexión."""
        try:
            with self._engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return True
        except Exception as e:
            print(f"❌ Error al probar la conexión: {e}")
            return False
