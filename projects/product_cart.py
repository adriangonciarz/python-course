class CartFullError(Exception):
    pass


class CodeInvalidError(Exception):
    pass


class Cart:
    max_items = 10
    promo_code = 'XYZ123'

    def __init__(self):
        self.products = []
        self.discounted = False

    def add_products(self, products):
        if isinstance(products, Product) and self._can_add_products_to_cart(1):
            self.products.append(products)
        elif isinstance(products, list) and self._can_add_products_to_cart(len(products)):
            self.products.extend(products)

    def _can_add_products_to_cart(self, number_of_products):
        if len(self.products) + number_of_products <= self.max_items:
            return True
        else:
            raise CartFullError('The cart is already full!')

    def calculate_total(self):
        total_items_price = sum([p.price for p in self.products])
        if self.discounted:
            return 0.8 * total_items_price
        else:
            return total_items_price

    def apply_discount(self, code):
        if code == self.promo_code:
            self.discounted = True
        else:
            raise CodeInvalidError(f'Provided promo code {code} is invalid!')

    def get_item_names(self):
        return [p.name for p in self.products]


class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name


def generate_products(number_of_products):
    return [Product('asd', 33.99) for _ in range(number_of_products)]


if __name__ == '__main__':
    dress = Product('Black Dress', 139.99)
    trousers = Product('Jeans Trousers', 229.99)
    tshirt = Product('T-shirt', 139.99)

    expected_price = (139.99 + 229.99 + 139.99) * 0.8

    cart = Cart()

    cart.add_products(dress)
    cart.add_products(generate_products(3))
    cart.add_products(generate_products(7))

    cart.apply_discount('XYZ123')
    total = cart.calculate_total()
    print(total)
    print(expected_price)
