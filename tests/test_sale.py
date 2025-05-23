from src.models.sale import Sale
from src.models.employee import Employee
from src.models.customer import Customer
from src.models.product import Product
from src.models.city import City
from src.models.country import Country
from src.models.category import Category

def test_sale_relationships():
    # Armar objetos relacionados
    country = Country(1, "Argentina", "AR")
    city = City(1, "Buenos Aires", "1000", country)
    employee = Employee(1, "Ana", "M", "Gómez", None, "F", None, city)
    customer = Customer(1, "Luis", "E", "Fernández", "Calle Falsa 123", city)
    category = Category(1, "Bebidas")
    product = Product(1, "Agua", 100.0, category, None, "A", "No", "No", 365)

    sale = Sale(
        sale_id=999,
        employee=employee,
        customer=customer,
        product=product,
        quantity=2,
        discount=0.1,
        total_price=180.0,
        sale_date="2024-01-01",
        transaction_number="ABC123"
    )

    assert sale._customer.full_name() == "Luis E. Fernández"
    assert sale._product._name == "Agua"
    assert str(sale).startswith("Sale(999")
