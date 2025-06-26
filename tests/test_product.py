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


def test_product_set_price_valid_data() -> None:
    product = Product(
        "product_name",
        "product_description",
        14.5,
        11
    )
    product.price = 15.1
    assert product.price == 15.1


def test_product_set_price_invalid_data(capsys) -> None:
    product = Product(
        "product_name",
        "product_description",
        14.5,
        11
    )
    product.price = -14.1
    captured = capsys.readouterr()
    assert product.price == 14.5
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_prosuvt_dict_init() -> None:
    dict = {
        "name": "product_name",
        "description": "product_description",
        "price": 14.5,
        "quantity": 10
    }
    product = Product.new_product(dict)

    assert product.name == "product_name"
    assert product.description == "product_description"
    assert product.price == 14.5
    assert product.quantity == 10
