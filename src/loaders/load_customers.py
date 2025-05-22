import csv
from src.models.customer import Customer
from src.models.city import City
from src.loaders.load_cities import load_cities_from_csv
from src.loaders.load_countries import load_countries_from_csv

def load_customers_from_csv(filepath: str, cities: list[City]) -> list[Customer]:
    customers = []
    cities_dict = {c._id: c for c in cities}

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city_id = int(row["CityID"])
            city = cities_dict.get(city_id)

            customer = Customer(
                customer_id=int(row["CustomerID"]),
                first_name=row["FirstName"],
                middle_initial=row["MiddleInitial"],
                last_name=row["LastName"],
                address=row["Address"],
                city=city
            )
            customers.append(customer)
    return customers

if __name__ == "__main__":
    countries = load_countries_from_csv("data/countries.csv")
    cities = load_cities_from_csv("data/cities.csv", countries)
    customers = load_customers_from_csv("data/customers.csv", cities)
    for c in customers[:10]:
        print(c)
