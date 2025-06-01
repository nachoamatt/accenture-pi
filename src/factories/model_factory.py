from src.models.category import Category
from src.models.city import City
from src.models.country import Country
from src.models.customer import Customer
from src.models.employee import Employee
from src.models.product import Product
from src.models.sale import Sale

class ModelFactory:
    @staticmethod
    def create(model_type: str, data: dict):
        if model_type == "Category":
            return Category(
                category_id=data["category_id"],
                name=data["name"]
            )
        elif model_type == "Country":
            return Country(
                country_id=data["country_id"],
                name=data["name"],
                code=data["code"]
            )
        elif model_type == "City":
            return City(
                city_id=data["city_id"],
                name=data["name"],
                zipcode=data["zipcode"],
                country=data["country"]
            )
        elif model_type == "Customer":
            return Customer(
                customer_id=data["customer_id"],
                first_name=data["first_name"],
                middle_initial=data["middle_initial"],
                last_name=data["last_name"],
                address=data["address"],
                city=data["city"]
            )
        elif model_type == "Employee":
            return Employee(
                employee_id=data["employee_id"],
                first_name=data["first_name"],
                middle_initial=data["middle_initial"],
                last_name=data["last_name"],
                birth_date=data["birth_date"],
                gender=data["gender"],
                hire_date=data["hire_date"],
                city=data["city"]
            )
        elif model_type == "Product":
            return Product(
                product_id=data["product_id"],
                name=data["name"],
                price=data["price"],
                category=data["category"],
                modify_date=data["modify_date"],
                product_class=data["product_class"],
                resistant=data["resistant"],
                is_allergic=data["is_allergic"],
                vitality_days=data["vitality_days"]
            )
        elif model_type == "Sale":
            return Sale(
                sale_id=data["sale_id"],
                employee=data["employee"],
                customer=data["customer"],
                product=data["product"],
                quantity=data["quantity"],
                discount=data["discount"],
                total_price=data["total_price"],
                sale_date=data["sale_date"],
                transaction_number=data["transaction_number"]
            )
        else:
            raise ValueError(f"Tipo de modelo desconocido: {model_type}")
