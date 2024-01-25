# task9.py

def robot_position(steps):
    # Вычисление координат робота после N шагов
    x = y = 0
    dx, dy = -1, 0
    for _ in range(steps):
        x, y = x + dx, y + dy
        if abs(x) == abs(y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
    return x, y

# Чтение количества шагов из файла
with open("input.txt", "r") as file:
    n = int(file.readline().strip())

# Получение и запись координат в файл
result = robot_position(n)
with open("output.txt", "w") as file:
    file.write(f"{result[0]} {result[1]}")

# Убедитесь, что файл input.txt существует в той же директории
