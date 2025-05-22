import csv
from src.models.city import City
from src.models.country import Country
from src.loaders.load_countries import load_countries_from_csv

def load_cities_from_csv(filepath: str, countries: list[Country]) -> list[City]:
    cities = []
    countries_dict = {c._id: c for c in countries}  

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country_id = int(row["CountryID"])
            country = countries_dict.get(country_id)

            city = City(
                city_id=int(row["CityID"]),
                name=row["CityName"],
                zipcode=row["Zipcode"],
                country=country
            )
            cities.append(city)
    return cities

if __name__ == "__main__":
    countries = load_countries_from_csv("data/countries.csv")
    cities = load_cities_from_csv("data/cities.csv", countries)
    for c in cities:
        print(c)
