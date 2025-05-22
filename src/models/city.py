# src/models/city.py

from src.models.country import Country

class City:
    def __init__(self, city_id: int, name: str, zipcode: str, country: Country):
        self._id = city_id
        self._name = name
        self._zipcode = zipcode
        self._country = country

    def __str__(self):
        return f"City({self._id}, '{self._name}', {self._country})"
