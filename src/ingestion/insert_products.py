from sqlalchemy import text
from src.loaders.load_products import load_products_from_csv
from src.loaders.load_categories import load_categories_from_csv
from src.db.connector import DatabaseConnector

def insert_products(filepath: str):
    connector = DatabaseConnector()
    categories = load_categories_from_csv("data/categories.csv")
    products = load_products_from_csv(filepath, categories)

    with connector.engine.begin() as conn:
        for product in products:
            conn.execute(
                text("""
                    REPLACE INTO products 
                    (product_id, name, price, category_id, modify_date, product_class, resistant, is_allergic, vitality_days)
                    VALUES (:id, :name, :price, :category_id, :modify_date, :product_class, :resistant, :is_allergic, :vitality_days)
                """),
                {
                    "id": product._id,
                    "name": product._name,
                    "price": product._price,
                    "category_id": product._category.get_id(),
                    "modify_date": product._modify_date,
                    "product_class": product._product_class,
                    "resistant": product._resistant,
                    "is_allergic": product._is_allergic,
                    "vitality_days": product._vitality_days
                }
            )

if __name__ == "__main__":
    csv_path = "data/products.csv"
    insert_products(csv_path)
