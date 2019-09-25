class NoSpaceInCartError(Exception):
    pass


class CodeInvalidError(Exception):
    pass


class Cart:
    max_items = 10
    promo_code = 'XYZ123'
    code_factor = 0.8

    def __init__(self):
        self.products = []
        self.discounted = False

    def add_products(self, products):
        if isinstance(products, Product) and self._can_add_items_to_cart(1):
            self.products.append(products)
        elif isinstance(products, list) and self._can_add_items_to_cart(len(products)):
            self.products.extend(products)

    def calculate_total(self):
        total_items_price = sum([p.price for p in self.products])
        if self.discounted:
            return self.code_factor * total_items_price
        else:
            return total_items_price

    def apply_discount(self, code):
        if code == self.promo_code:
            self.discounted = True
        else:
            raise CodeInvalidError(f'Provided promo code {code} is invalid!')

    def get_item_names(self):
        return [p.name for p in self.products]

    def _can_add_items_to_cart(self, no_of_items):
        if len(self.products) + no_of_items <= self.max_items:
            return True
        else:
            raise NoSpaceInCartError('The cart has not enough space for products')


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


if __name__ == '__main__':
    dress = Product('Black Dress', 139.99)
    trousers = Product('Jeans Trousers', 229.99)
    tshirt = Product('T-shirt', 139.99)

    cart = Cart()
    cart.add_product(dress)
    cart.add_product(trousers)
    cart.add_product(tshirt)
    cart.apply_discount('XYZ123')
    total = cart.calculate_total()
    print(total)
