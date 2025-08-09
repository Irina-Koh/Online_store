from src.product import Product
from src.catecory import Category




def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(first_category.products) == 2

    assert first_category.number_of_categories == 2
    assert second_category.number_of_categories == 2

    assert first_category.number_of_products == 3
    assert second_category.number_of_products == 3


def test_add_product():
    category = Category("Смартфоны", "Лучшие смартфоны на рынке", [])
    product = Product("iPhone 13", 999.99, 10, 11)
    category.add_product(product)
    assert len(category._products) == 1
    assert category._products[0] == product

def test_list_products():
    category = Category("Смартфоны", "Лучшие смартфоны на рынке", [])
    product1 = Product("iPhone 13", 999.99, 10, 15)
    product2 = Product("Samsung Galaxy S21", 899.99, 15, 20)
    category.add_product(product1)
    category.add_product(product2)
    expected_output = f"{product1.name} {product1.price} руб. {product1.quantity} шт.\\n{product2.name} {product2.price} руб. {product2.quantity} шт."
    assert category.list_products == expected_output