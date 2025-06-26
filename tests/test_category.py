from src.Category import Category


def test_category_init() -> None:
    category = Category(
        "cat_1",
        "cat_description_1",
        []
    )
    assert category.name == "cat_1"
    assert category.description == "cat_description_1"
    assert len(category.products) == 0


def test_category_class_vars(products_list) -> None:
    Category(
        "cat_1", "cat_desc_1", products_list[0:3]
    )
    Category(
        "cat_2", "cat_desc_2", [products_list[4]]
    )
    Category(
        "cat_3", "cat_desc_3", products_list[5:9]
    )
    assert Category.category_count == 3
    assert Category.product_count == 8


def test_category_class_vars_access(products_list) -> None:
    category1 = Category(
        "cat_1", "cat_desc_1", [products_list[0]]
    )
    category2 = Category(
        "cat_2", "cat_desc_2", products_list[1:3],
    )

    assert category1.product_count == category2.product_count
    assert category1.category_count == category2.category_count
