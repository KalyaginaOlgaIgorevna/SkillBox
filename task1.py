# task1.py

def validate_args(func):
    # Декоратор для валидации аргументов функции
    def wrapper(*args):
        # Проверка на количество аргументов
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        
        # Проверка типа аргумента
        if not isinstance(args[0], int):
            return "Wrong types"

        # Проверка на отрицательное значение
        if args[0] < 0:
            return "Negative argument"

        # Вызов оригинальной функции, если все проверки пройдены
        return func(*args)

    # Возвращение обертывающей функции
    return wrapper

# Пример функции, использующей декоратор
@validate_args
def some_function(x):
    return x * 2
print(some_function(5))          # Корректный вызов
print(some_function(-5))         # Отрицательный аргумент
print(some_function("string"))   # Некорректный тип аргумента
print(some_function())           # Недостаточно аргументов
print(some_function(1, 2))