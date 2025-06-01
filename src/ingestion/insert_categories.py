from sqlalchemy import text
from src.loaders.load_categories import load_categories_from_csv
from src.db.connector import DatabaseConnector

def insert_categories(filepath: str):
    connector = DatabaseConnector()
    categories = load_categories_from_csv(filepath)

    with connector.engine.begin() as conn:
        for category in categories:
            conn.execute(
                text("""
                    REPLACE INTO categories (category_id, name)
                    VALUES (:id, :name)
                """),
                {
                    "id": category.get_id(),
                    "name": category.get_name()
                }
            )

if __name__ == "__main__":
    csv_path = "data/categories.csv"
    insert_categories(csv_path)
