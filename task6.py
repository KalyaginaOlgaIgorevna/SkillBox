# task6.py

# Чтение списка слов из стандартного ввода
words = input().split()

# Вывод строки, составленной из последних букв каждого слова
print(''.join(word[-1] for word in words))

