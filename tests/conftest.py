import pytest

from src.Product import Product
from src.Category import Category


@pytest.fixture
def products_list() -> list[Product]:
    return [
        Product("p_1", "p_d_1", 1.1, 1),
        Product("p_2", "p_d_2", 1.2, 2),
        Product("p_3", "p_d_3", 1.3, 3),
        Product("p_4", "p_d_4", 1.4, 4),
        Product("p_5", "p_d_5", 1.5, 5),
        Product("p_6", "p_d_6", 1.6, 6),
        Product("p_7", "p_d_7", 1.7, 7),
        Product("p_8", "p_d_8", 1.8, 8),
        Product("p_9", "p_d_9", 1.9, 9),
        Product("p_10", "p_d_10", 2.0, 10),
    ]


@pytest.fixture(autouse=True)
def reset_class_var():
    Category.category_count = 0
    Category.product_count = 0
