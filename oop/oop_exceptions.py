class NotIntegerError(Exception):
    pass


class IdNotSetError(Exception):
    pass


class StoreItem:
    def __init__(self, name):
        self._item_id = None
        self._name = name

    @property
    def item_id(self):
        if self._item_id is None:
            raise IdNotSetError('Id is not set!')
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        if not isinstance(value, int):
            raise NotIntegerError('Provided ID value is not an integer!')
        self._item_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


if __name__ == '__main__':
    apple = StoreItem('Red Apple')
    apple.item_id = 1
    print(apple.item_id)
    print(apple.name)
