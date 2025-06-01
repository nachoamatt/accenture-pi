from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from dotenv import load_dotenv
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

        # Solo se requiere que user y database no estén vacíos
        if not all([user, database]):
            raise ValueError("Faltan variables necesarias en el archivo .env")

        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self._engine = create_engine(url)

    @property
    def engine(self) -> Engine:
        return self._engine
