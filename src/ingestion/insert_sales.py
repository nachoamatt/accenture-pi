from src.loaders.load_employees import load_employees_from_csv
from src.loaders.load_customers import load_customers_from_csv
from src.loaders.load_products import load_products_from_csv
from src.loaders.load_sales import load_sales_from_csv
from src.loaders.load_cities import load_cities_from_csv
from src.loaders.load_countries import load_countries_from_csv
from src.loaders.load_categories import load_categories_from_csv
from src.db.connector import DatabaseConnector
from sqlalchemy import text

def insert_sales(filepath: str):
    # Primero cargar todos los datos necesarios para las relaciones
    countries = load_countries_from_csv("data/countries.csv")
    cities = load_cities_from_csv("data/cities.csv", countries)
    customers = load_customers_from_csv("data/customers.csv", cities)
    employees = load_employees_from_csv("data/employees.csv", cities)
    categories = load_categories_from_csv("data/categories.csv")
    products = load_products_from_csv("data/products.csv", categories)

    sales = load_sales_from_csv(filepath, employees, customers, products)

    connector = DatabaseConnector()

    with connector.engine.begin() as conn:
        for sale in sales:
            conn.execute(
                text("""
                    REPLACE INTO sales (sale_id, employee_id, customer_id, product_id,
                        quantity, discount, total_price, sale_date, transaction_number)
                    VALUES (:sale_id, :employee_id, :customer_id, :product_id,
                        :quantity, :discount, :total_price, :sale_date, :transaction_number)
                """),
                {
                    "sale_id": sale._id,
                    "employee_id": sale._employee._id,
                    "customer_id": sale._customer._id,
                    "product_id": sale._product._id,
                    "quantity": sale._quantity,
                    "discount": sale._discount,
                    "total_price": sale._total_price,
                    "sale_date": sale._sale_date,
                    "transaction_number": sale._transaction_number
                }
            )

if __name__ == "__main__":
    csv_path = "data/sales.csv"
    insert_sales(csv_path)
