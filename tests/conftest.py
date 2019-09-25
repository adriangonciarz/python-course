import random

import pytest

from projects.product_cart import Product
from faker import Faker

fake = Faker()


@pytest.fixture
def single_product():
    return Product(fake.ean13(), round(random.random(), 2))
