import unittest
from src.keyboard import Keyboard


class TestKeyboard(unittest.TestCase):
    def setUp(self):
        self.keyboard = Keyboard("TestKeyboard", 50.0, 10)

    def test_initialization(self):
        self.assertEqual(self.keyboard.name, "TestKeyboard")
        self.assertEqual(self.keyboard.price, 50.0)
        self.assertEqual(self.keyboard.quantity, 10)
        self.assertEqual(self.keyboard.language, "EN")

    def test_change_language(self):
        self.assertEqual(self.keyboard.language, "EN")
        self.keyboard.change_lang()
        self.assertEqual(self.keyboard.language, "RU")
        self.keyboard.change_lang()
        self.assertEqual(self.keyboard.language, "EN")

    def test_name_property(self):
        self.assertEqual(self.keyboard.name, "TestKeyboard")
        self.keyboard.name = "Keyboard"
        self.assertEqual(self.keyboard.name, "Keyboard")

    def test_apply_discount(self):
        self.assertEqual(self.keyboard.price, 50.0)
        self.keyboard.pay_rate = 1.1
        self.keyboard.apply_discount()
        self.assertEqual(int(self.keyboard.price), 55)

    def test_string_to_number(self):
        self.assertEqual(Keyboard.string_to_number("25.5"), 25)


if __name__ == "__main__":
    unittest.main()
