# src/models/product.py

from src.models.category import Category

class Product:
    def __init__(self, product_id: int, name: str, price: float, category: Category,
                 modify_date, product_class: str, resistant: str, is_allergic: str, vitality_days: int):
        self._id = product_id
        self._name = name
        self._price = price
        self._category = category
        self._modify_date = modify_date
        self._product_class = product_class
        self._resistant = resistant
        self._is_allergic = is_allergic
        self._vitality_days = vitality_days

    def get_price(self):
        return self._price

    def apply_discount(self, percentage: float):
        self._price *= (1 - percentage / 100)

    def __str__(self):
        return f"Product({self._id}, {self._name}, ${self._price})"
