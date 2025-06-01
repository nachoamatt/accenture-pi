from sqlalchemy import text
from src.loaders.load_cities import load_cities_from_csv
from src.loaders.load_countries import load_countries_from_csv
from src.db.connector import DatabaseConnector

def insert_cities(filepath: str):
    connector = DatabaseConnector()
    countries = load_countries_from_csv("data/countries.csv")  # Necesitamos cargar países para asociar a ciudades
    cities = load_cities_from_csv(filepath, countries)

    with connector.engine.begin() as conn:
        for city in cities:
            conn.execute(
                text("""
                    REPLACE INTO cities (city_id, name, zipcode, country_id)
                    VALUES (:city_id, :name, :zipcode, :country_id)
                """),
                {
                    "city_id": city.id,
                    "name": city.name,
                    "zipcode": city.zipcode,
                    "country_id": city.country.id if city.country else None
                }
            )

if __name__ == "__main__":
    csv_path = "data/cities.csv"
    insert_cities(csv_path)
