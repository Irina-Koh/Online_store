class Category:
    """Класс для представления категории."""

    name: str
    description: str
    products: list
    number_of_categories = 0
    number_of_products = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self._products = products if products else []
        Category.number_of_categories += 1
        Category.number_of_products += len(self._products) if self._products else 0

    def add_product(self, product_new):
        self._products.append(product_new)
        self.product_count += 1

    @property
    def products(self):
        return "\\n".join(f"{product.name} {product.price} руб. {product.quantity} шт." for product in self._products)
