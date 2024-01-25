# task2.py

def memoize(func):
    # Словарь для хранения кэшированных результатов
    cache = {}

    def wrapper(n):
        # Проверка на наличие результата в кэше
        if n not in cache:
            # Вычисление и сохранение результата в кэше, если его нет
            cache[n] = func(n)
        # Возвращение кэшированного результата
        return cache[n]

    # Сохранение имени и документации оригинальной функции
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

# Пример функции Фибоначчи с использованием декоратора memoize
@memoize
def fibonacci(n):
    """Calculate Fibonacci number recursively."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))  # Вычисление 10-го числа Фибоначчи
print(fibonacci(20))  # Вычисление 20-го числа Фибоначчи