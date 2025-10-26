from src.product import Product
import pytest


def test_product_init(product, capsys):
    assert product.name == '55" QLED 4K'
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7
    with pytest.raises(ValueError) as excinfo:
        product_add = Product('56" QLED 4K', "Фоновая подсветка", 133000.0, 0)
    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"


def test_new_product():
    params_product = {"name": "iPhone 13", "description": "Лучший смартфон на рынке", "price": 999.99, "quantity": 10}
    product = Product.new_product(params_product)
    assert product.name == "iPhone 13"
    assert product.description == "Лучший смартфон на рынке"
    assert product.price == 999.99
    assert product.quantity == 10


def test_price_getter():
    product = Product("iPhone 13", "Лучший смартфон на рынке", 999.99, 10)
    assert product.price == 999.99


def test_price_setter_valid():
    product = Product("iPhone 13", "Лучший смартфон на рынке", 999.99, 10)
    product.price = 1099.99
    assert product.price == 1099.99


def test_price_setter_invalid():
    product = Product("iPhone 13", "Лучший смартфон на рынке", -100, 10)
    with pytest.raises(ValueError) as excinfo:
        product.price = -100
    assert str(excinfo.value) == "Цена не должна быть нулевой или отрицательной"


def test_product_str(product):
    assert str(product) == """55" QLED 4K, 123000.0 руб. Остаток: 7 шт."""


def test_product_add(product1, product2, product3, product5):
    assert product1 + product2 == 2580000.0
    with pytest.raises(TypeError) as excinfo:
        product1 + product3
    assert "Ошибка: Нельзя сложить Product и Smartphone." in str(excinfo.value)
    assert product3 + product5 == 12000000


def test_smartphone_init(product3):
    assert product3.name == "Samsung Galaxy"
    assert product3.description == "Флагманский смартфон"
    assert product3.price == 60000
    assert product3.quantity == 100
    assert product3.efficiency == "Высокая производительность"
    assert product3.model == "S23 Ultra"
    assert product3.memory == "512 ГБ"
    assert product3.color == "Чёрный"


def test_lawn_grass_init(product4):
    assert product4.name == "Газонная трава Экстра"
    assert product4.description == "Высококачественный сорт газонной травы"
    assert product4.price == 500
    assert product4.quantity == 100
    assert product4.country == "Голландия"
    assert product4.germination_period == "7-10 дней"
    assert product4.color == "Ярко-зеленый"
