# src/models/customer.py

from src.models.city import City

class Customer:
    def __init__(self, customer_id: int, first_name: str, middle_initial: str, last_name: str, address: str, city: City):
        self._id = customer_id
        self._first_name = first_name
        self._middle_initial = middle_initial
        self._last_name = last_name
        self._address = address
        self._city = city

    def full_name(self):
        return f"{self._first_name} {self._middle_initial}. {self._last_name}"

    def __str__(self):
        return f"Customer({self._id}, {self.full_name()})"
