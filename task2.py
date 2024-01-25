# task2.py
class DoubleElement:
    def __init__(self, *lst):
        # Сохраняем переданные аргументы в виде кортежа
        self.lst = lst
        # Инициализируем индекс для отслеживания текущего элемента
        self.index = 0

    def __next__(self):
        # Проверяем, не вышел ли индекс за пределы списка
        if self.index >= len(self.lst):
            # Если вышел, прерываем итерацию
            raise StopIteration
        # Проверяем, можно ли сформировать пару из двух элементов
        if self.index + 1 < len(self.lst):
            # Формируем пару из текущего и следующего элементов
            pair = (self.lst[self.index], self.lst[self.index + 1])
        else:
            # Если следующего элемента нет, второй элемент пары - None
            pair = (self.lst[self.index], None)
        # Увеличиваем индекс на два для следующей итерации
        self.index += 2
        return pair

    def __iter__(self):
        # Возвращаем объект в качестве итератора
        return self

# Создание экземпляра класса с четным количеством элементов
dL = DoubleElement(1, 2, 3, 4)
# Итерация по объекту и вывод пар элементов
for pair in dL:
    print(pair)

print()

# Создание экземпляра класса с нечетным количеством элементов
dL = DoubleElement(1, 2, 3, 4, 5)
# Итерация по объекту и вывод пар элементов
for pair in dL:
    print(pair)
