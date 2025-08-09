from src.product import Product
import pytest


def test_product_init(product):
    assert product.name == '55" QLED 4K'
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_new_product():
    params_product = {"name": "iPhone 13", "description": "Лучший смартфон на рынке", "price": 999.99, "quantity": 10}
    product = Product.new_product(params_product)
    assert product.name == "iPhone 13"
    assert product.description == "Лучший смартфон на рынке"
    assert product.price == 999.99
    assert product.quantity == 10


def test_price_getter():
    product = Product("iPhone 13", 999.99, 10)
    assert product.price == 999.99


def test_price_setter_valid():
    product = Product("iPhone 13", 999.99, 10)
    product.price = 1099.99
    assert product.price == 1099.99


def test_price_setter_invalid():
    product = Product("iPhone 13", 999.99, 10)
    with pytest.raises(ValueError):
        product.price = -100
