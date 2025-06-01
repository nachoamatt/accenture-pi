from src.models.employee import Employee
from src.models.customer import Customer
from src.models.product import Product

class Sale:
    def __init__(
        self,
        sale_id: int,
        employee: Employee,
        customer: Customer,
        product: Product,
        quantity: int,
        discount: float,
        total_price: float,
        sale_date,
        transaction_number: str
    ):
        self._id = sale_id
        self._employee = employee
        self._customer = customer
        self._product = product
        self._quantity = quantity
        self._discount = discount
        self._total_price = total_price
        self._sale_date = sale_date
        self._transaction_number = transaction_number

    @property
    def id(self):
        return self._id

    @property
    def employee(self):
        return self._employee

    @property
    def customer(self):
        return self._customer

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity

    @property
    def discount(self):
        return self._discount

    @property
    def total_price(self):
        return self._total_price

    @property
    def sale_date(self):
        return self._sale_date

    @property
    def transaction_number(self):
        return self._transaction_number

    def __str__(self):
        return f"Sale({self._id}, {self.customer.full_name()}, {self.product._name}, {self._total_price})"
