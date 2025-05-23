from src.models.customer import Customer
from src.models.city import City
from src.models.country import Country

def test_customer_full_name():
    country = Country(country_id=1, name="Argentina", code="AR")
    city = City(city_id=10, name="Buenos Aires", zipcode="1000", country=country)
    customer = Customer(
        customer_id=1,
        first_name="Juan",
        middle_initial="M",
        last_name="Pérez",
        address="Av. Siempreviva 123",
        city=city
    )

    assert customer.full_name() == "Juan M. Pérez"
    assert str(customer) == "Customer(1, Juan M. Pérez)"
