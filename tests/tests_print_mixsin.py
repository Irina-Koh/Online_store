from src.product import Product, Smartphone, LawnGrass


def test_print_mixin(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    Smartphone(
        name="Samsung Galaxy",
        description="Флагманский смартфон",
        price=60000,
        quantity=100,
        efficiency="Высокая производительность",
        model="S23 Ultra",
        memory="512 ГБ",
        color="Чёрный",
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy, Флагманский смартфон, 60000, 100)"

    LawnGrass(
        name="Газонная трава Экстра",
        description="Высококачественный сорт газонной травы",
        price=500,
        quantity=100,
        country="Голландия",
        germination_period="7-10 дней",
        color="Ярко-зеленый",
    )
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава Экстра, Высококачественный сорт газонной травы, 500, 100)"
