# task8.py

# Чтение номера телефона из стандартного ввода
phone = input()

# Удаление всех нечисловых символов и вывод
print(''.join(filter(str.isdigit, phone)))

