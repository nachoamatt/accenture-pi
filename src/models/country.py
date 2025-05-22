# src/models/country.py

class Country:
    def __init__(self, country_id: int, name: str, code: str):
        self._id = country_id
        self._name = name
        self._code = code

    def __str__(self):
        return f"Country({self._id}, '{self._name}', '{self._code}')"
