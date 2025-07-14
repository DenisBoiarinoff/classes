import pytest

from src.Category import Category
from src.LawnGrass import LawnGrass
from src.Product import Product
from src.Smartphone import Smartphone


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
    assert captured.out == ("Product('product_name', 'product_description', 14.5, 11)\nЦена не должна быть нулевая "
                            "или отрицательная\n")


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
    test_product = Product("test", "test", 0, 1)
    for product in products_list:
        total_sum += test_product + product
    assert total_sum == 93.5


@pytest.mark.parametrize(
    "left, right",
    [
        (
            Product("p_1", "p_1_d", 1.0, 2),
            Category("c_1", "c_1_d", [])
        ),
        (
            LawnGrass("lg_1", "lg_1_d", 2.0, 1, "-", "-", "-"),
            Smartphone("s_1", "s_1_d", "3.0", 1, "-", "-", 1, "1")
        ),
        (
            Product("p_1", "p_1_d", 1.0, 2),
            Smartphone("s_1", "s_1_d", "3.0", 1, "-", "-", 1, "1")
        ),
        (
            Product("p_1", "p_1_d", 1.0, 2),
            2
        ),
        (
            Product("p_1", "p_1_d", 1.0, 2),
            2.0
        ),
        (
            Product("p_1", "p_1_d", 1.0, 2),
            "2"
        )
    ]
)
def test_product_add_odd_data(left, right) -> None:
    with pytest.raises(TypeError):
        left + right


@pytest.mark.parametrize(
    "type_object, args, output",
    [
        (Product, ("p_1", "p_1_desc", 0, 1), "Product('p_1', 'p_1_desc', 0, 1)\n"),
        (Smartphone, ("s_1", "s_1_desc", 0, 1, "-", "-", 1, "1"), "Smartphone('s_1', 's_1_desc', 0, 1)\n"),
        (LawnGrass, ("lg_1", "lg_1_desc", 2.0, 1, "-", "-", "-"), "LawnGrass('lg_1', 'lg_1_desc', 2.0, 1)\n")

    ]
)
def test_product_init_log(capsys, type_object, args, output) -> None:
    type_object(*args)
    captured = capsys.readouterr()
    assert captured.out == output


@pytest.mark.parametrize(
    "type_object, args",
    [
        (Product, ("p_1", "p_1_desc", 0, 0)),
        (Smartphone, ("s_1", "s_1_desc", 0, 0, "-", "-", 1, "1")),
        (LawnGrass, ("lg_1", "lg_1_desc", 2.0, 0, "-", "-", "-"))

    ]
)
def test_product_invalid_quantity(type_object, args) -> None:
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        type_object(*args)
