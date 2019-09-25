from faker import Faker

fake = Faker('pl_PL')


class UserNotLoggedInException(Exception):
    pass


class User:
    api_key = 'jogRKWGfvNdgaR96RKPo2nYchLyPuXmu'
    company = 'RBS'

    def __init__(self, email):
        self.email = email
        self._first_name = fake.first_name()
        self._last_name = fake.last_name()
        self.__password = fake.password(length=20)
        self.__logged = False

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    def login(self, pwd):
        self.__logged = (pwd == self.__password)

    @property
    def is_logged(self):
        return self.__logged

    def set_password(self, key, pwd):
        if self.api_key == key:
            self.__password = pwd

    @staticmethod
    def say_hello():
        print('Hello! Nice to meet you!')

    @classmethod
    def describe_company(cls):
        print(f'{cls.company}')

    def pay(self):
        if self.__logged:
            print('I paid your bill')
        else:
            raise UserNotLoggedInException('User is not logged in and cannot pay!')


class Admin(User):
    def __init__(self, email, privileges):
        super().__init__(email)
        self.privileges = privileges


if __name__ == '__main__':
    u = User('agonciarz@example.com')
    print(u.first_name)
    u.first_name = 'Krzysztof'
    u.last_name = 'Ścierański'
    print(u.first_name)
    print(u.last_name)

    u.pay()

    print(u.is_logged)
    u.login('asdasd')
    print(u.is_logged)
    u.set_password(key='asdasd', pwd='haslo123')
    u.login('haslo123')
    print(u.is_logged)
    u.set_password(key='jogRKWGfvNdgaR96RKPo2nYchLyPuXmu', pwd='haslo123')
    u.login('haslo123')
    print(u.is_logged)

    u.say_hello()
    u.describe_company()
