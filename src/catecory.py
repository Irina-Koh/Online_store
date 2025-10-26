from src.product import Product


class Category:
    """Класс для представления категории."""

    name: str
    description: str
    products: list
    category_count = 0
    number_of_products = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self._products = products if products else []
        Category.category_count += 1
        Category.number_of_products += len(self._products) if self._products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self._products)} шт."

    def add_product(self, product_new):
        if isinstance(product_new, Product):
            self._products.append(product_new)
        else:
            raise TypeError(f'Объект "{product_new}" не является продуктом.')
        self.product_count += 1

    def middle_price(self):
        if len(self._products) == 0:
            return 0

        total_sum = sum(product._price for product in self._products)
        try:
            avg_price = total_sum / len(self._products)
            return avg_price
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        return "\\n".join(str(product) for product in self._products)
