from src.catecory import Category
from src.product import Product, Smartphone, LawnGrass

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Smartphone(
        name="Samsung Galaxy",
        description="Флагманский смартфон",
        price=60000,
        quantity=100,
        efficiency="Высокая производительность",
        model="S23 Ultra",
        memory="512 ГБ",
        color="Чёрный",
    )
    product5 = LawnGrass(
        name="Газонная трава 'Экстра'",
        description="Высококачественный сорт газонной травы.",
        price=500,
        quantity=100,
        country="Голландия",
        germination_period="7-10 дней",
        color="Ярко-зеленый",
    )
    product6 = Smartphone(
        name="Samsung Galaxy",
        description="Флагманский смартфон",
        price=60000,
        quantity=100,
        efficiency="Высокая производительность",
        model="S24 Ultra",
        memory="515 ГБ",
        color="Красный",
    )

    print(str(product1))
    print(str(product2))
    print(str(product3))
    print(str(product4))
    print(str(product5))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
    print(product4 + product6)
