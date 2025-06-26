from src.Product import Product


def test_product_init() -> None:
    product = Product(
        "product_name",
        "product_description",
        14.5,
        11
    )
    assert product.name == "product_name"
    assert product.description == "product_description"
    assert product.price == 14.5
    assert product.quantity == 11
