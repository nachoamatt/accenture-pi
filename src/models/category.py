# src/models/category.py

class Category:
    def __init__(self, category_id: int, name: str):
        self._id = category_id
        self._name = name

    def __str__(self):
        return f"Category({self._id}, '{self._name}')"

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
