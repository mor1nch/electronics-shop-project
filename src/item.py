from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return str(self.__name)

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Phone object must be of type Item")
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, path):
        try:
            with open(path, "r", encoding="utf-8") as csvfile:
                reader = DictReader(csvfile)
                for row in reader:
                    try:
                        name = row["name"]
                        price = float(row["price"])
                        quantity = int(row["quantity"])
                        cls(name, price, quantity)
                    except Exception:
                        raise InstantiateCSVError(path)
        except FileNotFoundError:
            print(f"Отсутствует файл {path}")

    @staticmethod
    def string_to_number(number: str) -> int:
        try:
            return int(number.split(".")[0])
        except ValueError:
            raise ValueError("Строка не содержит число до точки")


class InstantiateCSVError(Exception):
    def __init__(self, path):
        super().__init__(f"Файл {path} поврежден")
