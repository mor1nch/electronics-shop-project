from src.item import Item, InstantiateCSVError

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


def test_calculate_price():
    item1 = Item("Phone1", 20000, 3)
    item2 = Item("Phone2", 30000, 5)
    assert item1.price + item2.price == 50000


def test_instantiate_from_csv_file_not_found():
    try:
        Item.instantiate_from_csv('unknown_path')
    except FileNotFoundError:
        assert 1 == 1


def test_instantiate_from_csv_file_not_correct():
    try:
        Item.instantiate_from_csv('../src/failed_items.csv')
    except InstantiateCSVError:
        assert 1 == 1
