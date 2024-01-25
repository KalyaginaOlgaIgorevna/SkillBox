# task7.py

# Чтение списка чисел из стандартного ввода
numbers = list(map(int, input().split()))

# Вывод True, если есть дубликаты, иначе False
print(len(numbers) != len(set(numbers)))

