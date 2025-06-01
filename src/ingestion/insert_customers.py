from sqlalchemy import text
from src.loaders.load_customers import load_customers_from_csv
from src.loaders.load_cities import load_cities_from_csv
from src.loaders.load_countries import load_countries_from_csv
from src.db.connector import DatabaseConnector

def insert_customers(filepath: str):
    connector = DatabaseConnector()
    
    # Primero cargo países y ciudades
    countries = load_countries_from_csv("data/countries.csv")
    cities = load_cities_from_csv("data/cities.csv", countries)
    
    # Ahora cargo los clientes, pasando las ciudades
    customers = load_customers_from_csv(filepath, cities)

    with connector.engine.begin() as conn:
        for customer in customers:
            conn.execute(
                text("""
                    REPLACE INTO customers (customer_id, first_name, middle_initial, last_name, address, city_id)
                    VALUES (:id, :first_name, :middle_initial, :last_name, :address, :city_id)
                """),
                {
                    "id": customer._id,
                    "first_name": customer._first_name,
                    "middle_initial": customer._middle_initial,
                    "last_name": customer._last_name,
                    "address": customer._address,
                    "city_id": customer._city._id if customer._city else None
                }
            )

if __name__ == "__main__":
    csv_path = "data/customers.csv"
    insert_customers(csv_path)
