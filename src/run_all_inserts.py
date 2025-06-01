from src.ingestion.insert_countries import insert_countries
from src.ingestion.insert_cities import insert_cities
from src.ingestion.insert_customers import insert_customers
from src.ingestion.insert_employees import insert_employees
from src.ingestion.insert_categories import insert_categories
from src.ingestion.insert_products import insert_products
from src.ingestion.insert_sales import insert_sales

def run_all_inserts():
    inserts = [
        ("Countries", insert_countries, "data/countries.csv"),
        ("Cities", insert_cities, "data/cities.csv"),
        ("Customers", insert_customers, "data/customers.csv"),
        ("Employees", insert_employees, "data/employees.csv"),
        ("Categories", insert_categories, "data/categories.csv"),
        ("Products", insert_products, "data/products.csv"),
        ("Sales", insert_sales, "data/sales.csv")
    ]

    for name, func, path in inserts:
        try:
            print(f"Iniciando carga de {name}...")
            func(path)
            print(f"✅ Carga de {name} completada correctamente.\n")
        except Exception as e:
            print(f"❌ Error durante la carga de {name}: {e}\n")

if __name__ == "__main__":
    run_all_inserts()
