class Car:
    def __init__(self):
        self.__set_max_speed()
        self._speed = 0

    def __str__(self):
        return f'My max speed is {self.max_speed} kph'

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    def __set_max_speed(self):
        self.__max_speed = 200


if __name__ == '__main__':
    alfa_romeo = Car()
    alfa_romeo.__max_speed = 300
    print(alfa_romeo.max_speed)

    print(alfa_romeo.speed)
    print(str(alfa_romeo))
