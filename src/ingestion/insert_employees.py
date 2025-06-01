from sqlalchemy import text
from src.loaders.load_employees import load_employees_from_csv
from src.loaders.load_cities import load_cities_from_csv
from src.loaders.load_countries import load_countries_from_csv
from src.db.connector import DatabaseConnector

def insert_employees(filepath: str):
    connector = DatabaseConnector()
    
    # Cargo países y ciudades para pasarlos a la función loader de empleados
    countries = load_countries_from_csv("data/countries.csv")
    cities = load_cities_from_csv("data/cities.csv", countries)
    
    employees = load_employees_from_csv(filepath, cities)

    with connector.engine.begin() as conn:
        for employee in employees:
            conn.execute(
                text("""
                    INSERT INTO employees (
                        employee_id, first_name, middle_initial, last_name,
                        birth_date, gender, hire_date, city_id
                    ) VALUES (
                        :id, :first_name, :middle_initial, :last_name,
                        :birth_date, :gender, :hire_date, :city_id
                    )
                    ON DUPLICATE KEY UPDATE
                        first_name = VALUES(first_name),
                        middle_initial = VALUES(middle_initial),
                        last_name = VALUES(last_name),
                        birth_date = VALUES(birth_date),
                        gender = VALUES(gender),
                        hire_date = VALUES(hire_date),
                        city_id = VALUES(city_id)
                """),
                {
                    "id": employee._id,
                    "first_name": employee._first_name,
                    "middle_initial": employee._middle_initial,
                    "last_name": employee._last_name,
                    "birth_date": employee._birth_date,
                    "gender": employee._gender,
                    "hire_date": employee._hire_date,
                    "city_id": employee._city._id if employee._city else None
                }
            )

if __name__ == "__main__":
    csv_path = "data/employees.csv"
    insert_employees(csv_path)
