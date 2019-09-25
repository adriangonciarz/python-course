import random

import pytest

from projects.product_cart import Product, Cart, NoSpaceInCartError, CodeInvalidError
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
        assert c.products_count == 0

    def test_new_cart_is_not_discounted(self):
        c = Cart()
        assert c.is_discounted is False

    def test_adding_single_product(self, single_product):
        c = Cart()
        c.add_products(single_product)
        assert c.get_item_names() == [single_product.name]
        assert c.calculate_total() == single_product.price

    def test_adding_multiple_products(self):
        c = Cart()
        p1 = Product(fake.ean13(), round(random.random(), 2))
        p2 = Product(fake.ean13(), round(random.random(), 2))
        c.add_products([p1, p2])
        assert c.products_count == 2
        assert c.calculate_total() == p1.price + p2.price

    def test_adding_10_products_to_empty_cart(self):
        c = Cart()
        products = [Product(fake.ean13(), round(random.random(), 2)) for _ in range(10)]
        c.add_products(products)
        assert c.products_count == 10

    def test_adding_more_than_10_products_to_empty_cart(self):
        c = Cart()
        products = [Product(fake.ean13(), round(random.random(), 2)) for _ in range(11)]
        with pytest.raises(NoSpaceInCartError):
            c.add_products(products)

    def test_apply_valid_discount(self):
        c = Cart()
        c.apply_discount('XYZ123')
        assert c.is_discounted is True

    def test_apply_invalid_discount(self):
        c = Cart()
        with pytest.raises(CodeInvalidError):
            c.apply_discount('wrong123')
        assert c.is_discounted is False

    def test_calculate_with_discount(self):
        c = Cart()
        p1 = Product(fake.ean13(), round(random.random(), 2))
        p2 = Product(fake.ean13(), round(random.random(), 2))
        c.add_products([p1, p2])
        c.apply_discount('XYZ123')
        actual_price = c.calculate_total()
        expected_price = (p1.price + p2.price) * 0.8

        assert actual_price == expected_price

    def test_clearing_cart(self):
        c = Cart()
        p1 = Product(fake.ean13(), round(random.random(), 2))
        p2 = Product(fake.ean13(), round(random.random(), 2))
        c.add_products([p1, p2])
        c.clear()

        assert c.products_count == 0