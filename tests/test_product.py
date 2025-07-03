import pytest

from src.Product import Product


def test_product_init() -> None:
    product = Product("product_name", "product_description", 14.5, 11)
    assert product.name == "product_name"
    assert product.description == "product_description"
    assert product.price == 14.5
    assert product.quantity == 11


def test_product_set_price_valid_data() -> None:
    product = Product("product_name", "product_description", 14.5, 11)
    product.price = 15.1
    assert product.price == 15.1


def test_product_set_price_invalid_data(capsys) -> None:
    product = Product("product_name", "product_description", 14.5, 11)
    product.price = -14.1
    captured = capsys.readouterr()
    assert product.price == 14.5
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_product_dict_init() -> None:
    dict = {"name": "product_name", "description": "product_description", "price": 14.5, "quantity": 10}
    product = Product.new_product(dict)

    assert product.name == "product_name"
    assert product.description == "product_description"
    assert product.price == 14.5
    assert product.quantity == 10


@pytest.mark.parametrize(
    "list, index, output",
    [
        ("products_list", 0, "p_1, 1.1 руб. Остаток: 1 шт."),
        ("products_list", 1, "p_2, 1.2 руб. Остаток: 2 шт."),
        ("products_list", 2, "p_3, 1.3 руб. Остаток: 3 шт."),
        ("products_list", 3, "p_4, 1.4 руб. Остаток: 4 шт."),
        ("products_list", 4, "p_5, 1.5 руб. Остаток: 5 шт."),
    ],
)
def test_product_str(list, index, output, request) -> None:
    items = request.getfixturevalue(list)
    out = str(items[index])
    assert out == output


def test_product_add(products_list) -> None:
    total_sum = 0
    test_product = Product("test", "test", 0, 0)
    for product in products_list:
        total_sum += test_product + product
    assert total_sum == 93.5
