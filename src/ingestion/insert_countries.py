from sqlalchemy import text
from src.loaders.load_countries import load_countries_from_csv
from src.db.connector import DatabaseConnector

def insert_countries(filepath: str):
    connector = DatabaseConnector()
    countries = load_countries_from_csv(filepath)

    with connector.engine.begin() as conn:
        for country in countries:
            conn.execute(
                text("""
                    REPLACE INTO countries (country_id, name, code)
                    VALUES (:id, :name, :code)
                """),
                {
                    "id": country.id,
                    "name": country.name,
                    "code": country.code
                }
            )

if __name__ == "__main__":
    csv_path = "data/countries.csv"
    insert_countries(csv_path)
