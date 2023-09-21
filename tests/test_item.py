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
