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

    def add_product(self, product):
        if len(self.products) < self.max_items:
            self.products.append(product)
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
