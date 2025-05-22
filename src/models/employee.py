# src/models/employee.py

from src.models.city import City

class Employee:
    def __init__(self, employee_id: int, first_name: str, middle_initial: str, last_name: str,
                 birth_date, gender: str, hire_date, city: City):
        self._id = employee_id
        self._first_name = first_name
        self._middle_initial = middle_initial
        self._last_name = last_name
        self._birth_date = birth_date
        self._gender = gender
        self._hire_date = hire_date
        self._city = city

    def full_name(self):
        return f"{self._first_name} {self._middle_initial}. {self._last_name}"

    def __str__(self):
        return f"Employee({self._id}, {self.full_name()})"
