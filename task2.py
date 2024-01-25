# task2.py
# Чтение числа из стандартного ввода
a = int(input())
b,c,d = bin(a), oct(a), hex(a)
print(b[2:], c[2:], d[2:])

