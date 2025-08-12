import json
import os
from src.product import Product
from src.catecory import Category


def read_json(path: str) -> dict:
    """
    Читает содержимое JSON-файла и возвращает словарь.

    :param path: Относительный или абсолютный путь к файлу
    :return: Содержимое файла в виде словаря
    """
    try:
        full_path = os.path.abspath(path)

        # Проверяем существование файла перед открытием
        if not os.path.isfile(full_path):
            raise FileNotFoundError(f"Файл '{full_path}' не найден")

        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return {}


def list_products_and_category_from_json(data: dict) -> list:
    """
    Читает содержимое словаря, возращает список категорий
    :param data: словарь
    :return: список категорий
    """
    categories = []
    for category_data in data:
        products = []
        for product in category_data["products"]:
            products.append(Product(**product))
        category_data["products"] = products
        categories.append(Category(**category_data))
    return categories


if __name__ == "__main__":
    patch = "../src/products.json"
    read_data = read_json(patch)
    list_category = list_products_and_category_from_json(read_data)
    print(list_category)
