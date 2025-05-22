import csv
from src.models.country import Country

def load_countries_from_csv(filepath: str) -> list[Country]:
    countries = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country = Country(
                country_id=int(row["CountryID"]),
                name=row["CountryName"],
                code=row["CountryCode"]
            )
            countries.append(country)
    return countries

if __name__ == "__main__":
    countries = load_countries_from_csv("data/countries.csv")
    for c in countries:
        print(c)
