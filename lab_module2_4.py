class Car:
    def __init__(self, make: str, model: str, year: int):
        """
        Конструктор базового класса Car.

        :param make: Производитель автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """
        Метод, который возвращает сообщение о запуске двигателя.
        """
        return f"{self.make} {self.model} (Год: {self.year}): Двигатель запущен."

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Car.
        """
        return f"{self.__class__.__name__}(Производитель: {self.make}, Модель: {self.model}, Год: {self.year})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта Car.
        """
        return f"{self.__class__.__name__}(make='{self.make}', model='{self.model}', year={self.year})"


class PassengerCar(Car):
    def __init__(self, make: str, model: str, year: int, num_doors: int):
        """
        Конструктор дочернего класса PassengerCar. Расширяет конструктор базового класса Car.

        :param make: Производитель легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param num_doors: Количество дверей в легковом автомобиле.
        """
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def start_engine(self) -> str:
        """
        Метод, который возвращает сообщение о запуске двигателя с учетом типа автомобиля.
        """
        return f"{super().start_engine()} Это легковой автомобиль с {self.num_doors} дверями."

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта PassengerCar, включая количество дверей.
        """
        return f"{super().__str__()}, Количество дверей: {self.num_doors}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта PassengerCar, включая количество дверей.
        """
        return f"{super().__repr__()}, num_doors={self.num_doors}"


class Truck(Car):
    def __init__(self, make: str, model: str, year: int, payload_capacity: float):
        """
        Конструктор дочернего класса Truck. Расширяет конструктор базового класса Car.

        :param make: Производитель грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param payload_capacity: Грузоподъемность грузового автомобиля в тоннах.
        """
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def start_engine(self) -> str:
        """
        Метод, который возвращает сообщение о запуске двигателя с учетом типа автомобиля.
        """
        return f"{super().start_engine()} Это грузовой автомобиль с грузоподъемностью {self.payload_capacity} тонн."

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Truck, включая грузоподъемность.
        """
        return f"{super().__str__()}, Грузоподъемность: {self.payload_capacity} тонн"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта Truck, включая грузоподъемность.
        """
        return f"{super().__repr__()}, payload_capacity={self.payload_capacity}"


""""
• Car - базовый класс с атрибутами make, model и year, а также методом для запуска двигателя и строковым представлением.

• PassengerCar - дочерний класс, который наследует от Car, добавляет атрибут num_doors и переопределяет метод start_engine, чтобы включать информацию о количестве дверей.

• Truck - дочерний класс, который наследует от Car, добавляет атрибут payload_capacity и переопределяет метод start_engine, чтобы включать информацию о грузоподъемности.

"""