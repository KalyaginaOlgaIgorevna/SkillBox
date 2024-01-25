class Transport:
    # Основной класс для всех видов транспорта
    def __init__(self, coordinates, speed, brand, year, number):
        # Инициализация основных атрибутов транспортного средства
        self._coordinates = coordinates  # координаты транспорта
        self._speed = speed  # скорость транспорта
        self._brand = brand  # марка транспорта
        self._year = year  # год выпуска транспорта
        self._number = number  # номер транспорта

    def __str__(self):
        # Строковое представление объекта
        return f"Transport: {self._brand}, Year: {self._year}, Number: {self._number}"

    def isInArea(self, pos_x, pos_y, length, width):
        # Проверка, находится ли транспорт в заданной области
        x, y = self._coordinates
        return pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width

    # Геттеры и сеттеры для атрибутов
    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

# Классы для пассажирских и грузовых транспортных средств
class Passenger:
    # Класс для пассажирских транспортных средств
    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self._passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self._number_of_passengers = number_of_passengers

class Cargo:
    # Класс для грузовых транспортных средств
    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        self._carrying = carrying

# Классы для различных видов транспорта
class Plane(Transport):
    # Класс для самолетов
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height  # высота полета самолета

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

class Auto(Transport):
    # Базовый класс для автомобильного транспорта
    pass

class Ship(Transport):
    # Класс для кораблей
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port  # порт, в котором находится корабль

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

# Производные классы для конкретных видов автомобильного и корабельного транспорта
class Car(Auto):
    pass

class Bus(Auto, Passenger):
    pass

class CargoAuto(Auto, Cargo):
    pass

class Boat(Ship):
    pass

class PassengerShip(Ship, Passenger):
    pass

class CargoShip(Ship, Cargo):
    pass

class Seaplane(Plane, Ship):
    # Класс для гидросамолетов
    pass

# Пример использования классов (создание экземпляров, изменение атрибутов и вывод информации)