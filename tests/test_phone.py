import unittest

from src.phone import Phone


class TestPhone(unittest.TestCase):
    phone1 = Phone("iPhone 14", 75000, 50, 2)
    phone2 = Phone("Samsung S23", 60000, 20, 3)

    def test_phone_name(self):
        assert str(self.phone1) == "iPhone 14"
        assert str(self.phone2) == "Samsung S23"

    def test_phone_price(self):
        assert self.phone1.price == 75000
        assert self.phone2.price == 60000
        assert self.phone1.price + self.phone2.price == 135000

    def test_phone_number_of_sim(self):
        assert self.phone1.number_of_sim == 2

        try:
            self.phone1.number_of_sim = 0
        except ValueError:
            self.phone1.number_of_sim = 1

        assert self.phone1.number_of_sim == 1
