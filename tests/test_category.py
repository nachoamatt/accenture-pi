from src.models.category import Category

def test_category_creation():
    category = Category(category_id=99, name="Snacks")

    assert category.get_id() == 99
    assert category.get_name() == "Snacks"
    assert str(category) == "Category(99, 'Snacks')"
