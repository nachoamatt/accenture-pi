# src/loaders/load_categories.py

import csv
from src.models.category import Category

def load_categories_from_csv(filepath: str) -> list[Category]:
    categories = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = Category(
                category_id=int(row["CategoryID"]),
                name=row["CategoryName"],
            )
            categories.append(category)
    return categories

if __name__ == "__main__":
    ruta = "data/categories.csv"  # Ruta relativa desde la raíz del proyecto
    categorias = load_categories_from_csv(ruta)
    for c in categorias:
        print(c)
