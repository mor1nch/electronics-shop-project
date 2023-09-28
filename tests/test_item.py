from src.item import Item

item1 = Item(name="Apple", quantity=10, price=15.5)
item2 = Item(name="Banana", quantity=7, price=40)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 155
    assert item2.calculate_total_price() == 280


def test_apply_discount():
    assert item1.calculate_total_price() == 155
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.calculate_total_price() == 124


def test_property_name():
    assert item1.name == "Apple"
    item1.name = "Orange"
    assert item1.name == "Orange"


def test_string_to_number():
    assert Item.string_to_number("10.11111") == 10
    assert Item.string_to_number("11.9") == 11
    assert Item.string_to_number("12") == 12
    assert Item.string_to_number("0.1") == 0


def test_magic_methods():
    item1 = Item("Макбук м2", 200000, 3)
    assert repr(item1) == "Item('Макбук м2', 200000, 3)"
    assert str(item1) == 'Макбук м2'
    item1.name = 'Макбук м3'
    assert str(item1) == 'Макбук м3'
    item1.quantity = 4
    assert repr(item1) == "Item('Макбук м3', 200000, 4)"

