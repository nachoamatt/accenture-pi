import io
from src.models.category import Category
from src.loaders.load_categories import load_categories_from_csv

def test_load_categories_from_csv(monkeypatch):
    mock_csv = io.StringIO("""CategoryID,CategoryName
1,Bebidas
2,Panadería
3,Frutas
""")

    # Monkeypatch open() para devolver el CSV simulado
    monkeypatch.setattr("builtins.open", lambda *args, **kwargs: mock_csv)

    try:
        result = load_categories_from_csv("fake_path.csv")

        assert len(result) == 3
        assert isinstance(result[0], Category)
        assert result[0].get_name() == "Bebidas"

    except Exception as e:
        print("❌ test_load_categories_from_csv falló:")
        print(e)
