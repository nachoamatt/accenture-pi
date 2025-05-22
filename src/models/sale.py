# src/models/sale.py

from src.models.employee import Employee
from src.models.customer import Customer
from src.models.product import Product

class Sale:
    def __init__(self, sale_id: int, employee: Employee, customer: Customer, product: Product,
                 quantity: int, discount: float, total_price: float, sale_date, transaction_number: str):
        self._id = sale_id
        self._employee = employee
        self._customer = customer
        self._product = product
        self._quantity = quantity
        self._discount = discount
        self._total_price = total_price
        self._sale_date = sale_date
        self._transaction_number = transaction_number

    def __str__(self):
        return f"Sale({self._id}, {self._customer.full_name()}, {self._product._name}, {self._total_price})"
