import csv
from datetime import datetime
from src.models.category import Category
from src.models.product import Product
from src.factories.model_factory import ModelFactory

def load_products_from_csv(filepath: str, categories: list[Category]) -> list[Product]:
    products = []
    categories_dict = {c.get_id(): c for c in categories}

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category_id = int(row["CategoryID"])
            category = categories_dict.get(category_id)

            modify_date = None
            if row["ModifyDate"]:
                try:
                    modify_date = datetime.strptime(row["ModifyDate"], "%Y-%m-%d")
                except ValueError:
                    pass

            product_data = {
                "product_id": int(row["ProductID"]),
                "name": row["ProductName"],
                "price": float(row["Price"]),
                "category": category,
                "modify_date": modify_date,
                "product_class": row["Class"],
                "resistant": row["Resistant"],
                "is_allergic": row["IsAllergic"],
                "vitality_days": int(row["VitalityDays"])
            }

            product = ModelFactory.create("Product", product_data)
            products.append(product)

    return products

if __name__ == "__main__":
    from src.loaders.load_categories import load_categories_from_csv
    categories = load_categories_from_csv("data/categories.csv")
    products = load_products_from_csv("data/products.csv", categories)
    for p in products:
        print(p)
