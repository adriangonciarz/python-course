import random

from projects.product_cart import Product, Cart
from faker import Faker

fake = Faker()


class TestProducts:
    def test_product_name(self):
        p = Product('Black Dress', 99.99)
        assert p.name == 'Black Dress'

    def test_product_price(self):
        p = Product('Black Dress', 99.99)
        assert p.price == 99.99


class TestCart:
    def test_new_cart_empty(self):
        c = Cart()
        assert c.get_item_names() == []

    def test_adding_single_product(self):
        c = Cart()
        p = Product(fake.ean13(), round(random.random(), 2))
        c.add_product(p)
        assert c.get_item_names() == [p.name]
        assert c.calculate_total() == p.price

    def test_adding_multiple_products(self):
        c = Cart()
        p1 = Product(fake.ean13(), round(random.random(), 2))
        p2 = Product(fake.ean13(), round(random.random(), 2))
        c.add_product()
        assert c.get_item_names() == [p.name]
        assert c.calculate_total() == p.price
