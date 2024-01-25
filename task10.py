# task10.py

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Чтение размера матрицы
size = int(input())

# Создание исходной матрицы
matrix = [[i + 1 for i in range(size)] for _ in range(size)]

# Транспонирование матрицы
transposed = transpose(matrix)

# Вывод исходной и транспонированной матриц
print("Исходная матрица:")
for row in matrix:
    print(', '.join(map(str, row)))

print("\nТранспонированная матрица:")
for row in transposed:
    print(', '.join(map(str, row)))

