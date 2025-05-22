import csv
from datetime import datetime
from src.models.employee import Employee
from src.models.city import City
from src.loaders.load_cities import load_cities_from_csv
from src.loaders.load_countries import load_countries_from_csv

def load_employees_from_csv(filepath: str, cities: list[City]) -> list[Employee]:
    employees = []
    cities_dict = {c._id: c for c in cities}

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city = cities_dict.get(int(row["CityID"]))

            # Parse fechas
            birth_date = datetime.strptime(row["BirthDate"], "%Y-%m-%d %H:%M:%S.%f")
            hire_date = datetime.strptime(row["HireDate"], "%Y-%m-%d %H:%M:%S.%f")


            employee = Employee(
                employee_id=int(row["EmployeeID"]),
                first_name=row["FirstName"],
                middle_initial=row["MiddleInitial"],
                last_name=row["LastName"],
                birth_date=birth_date,
                gender=row["Gender"],
                hire_date=hire_date,
                city=city
            )
            employees.append(employee)
    return employees

if __name__ == "__main__":
    countries = load_countries_from_csv("data/countries.csv")
    cities = load_cities_from_csv("data/cities.csv", countries)
    employees = load_employees_from_csv("data/employees.csv", cities)
    for e in employees[:10]:
        print(e)
