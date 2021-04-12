class NegativeDigitException(ValueError):
    pass


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        if a < 0 or b < 0:
            raise NegativeDigitException

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

        if a < 0:
            raise NegativeDigitException

    def get_area_square(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

        if r < 0:
            raise NegativeDigitException

    def get_rad(self):
        return 3.14 * self.r ** 2
