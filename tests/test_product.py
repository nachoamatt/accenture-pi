from src.models.product import Product
from src.models.category import Category

def test_product_creation_and_discount():
    # Arrange
    category = Category(category_id=1, name="Bebidas")
    product = Product(
        product_id=101,
        name="Agua mineral",
        price=100.0,
        category=category,
        modify_date=None,
        product_class="A",
        resistant="No",
        is_allergic="No",
        vitality_days=365
    )

    # Assert initial price
    assert product.get_price() == 100.0

    # Act: apply discount
    product.apply_discount(10)  # 10%

    # Assert discounted price
    assert round(product.get_price(), 2) == 90.0
