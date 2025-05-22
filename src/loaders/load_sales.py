import csv
from src.models.sale import Sale
from src.models.employee import Employee
from src.models.customer import Customer
from src.models.product import Product
from src.loaders.load_employees import load_employees_from_csv
from src.loaders.load_customers import load_customers_from_csv
from src.loaders.load_products import load_products_from_csv
from src.loaders.load_cities import load_cities_from_csv
from src.loaders.load_countries import load_countries_from_csv
from src.loaders.load_categories import load_categories_from_csv

def load_sales_from_csv(filepath: str, employees: list[Employee], customers: list[Customer], products: list[Product]) -> list[Sale]:
    sales = []

    employee_dict = {e._id: e for e in employees}
    customer_dict = {c._id: c for c in customers}
    product_dict = {p._id: p for p in products}

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            employee = employee_dict.get(int(row["SalesPersonID"]))
            customer = customer_dict.get(int(row["CustomerID"]))
            product = product_dict.get(int(row["ProductID"]))

            sale = Sale(
                sale_id=int(row["SalesID"]),
                employee=employee,
                customer=customer,
                product=product,
                quantity=int(row["Quantity"]),
                discount=float(row["Discount"]),
                total_price=float(row["TotalPrice"]),
                sale_date=row["SalesDate"],  # tratamos como string por ahora
                transaction_number=row["TransactionNumber"]
            )
            sales.append(sale)
    return sales

if __name__ == "__main__":
    countries = load_countries_from_csv("data/countries.csv")
    cities = load_cities_from_csv("data/cities.csv", countries)
    customers = load_customers_from_csv("data/customers.csv", cities)
    employees = load_employees_from_csv("data/employees.csv", cities)
    categories = load_categories_from_csv("data/categories.csv")
    products = load_products_from_csv("data/products.csv", categories)
    sales = load_sales_from_csv("data/sales.csv", employees, customers, products)

    for s in sales[:10]:
        print(s)
