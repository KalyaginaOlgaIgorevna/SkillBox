# task11.py

def check_winner(board):
    n = len(board)
    rows = columns = [0] * n
    diag = anti_diag = 0

    for i in range(n):
        for j in range(n):
            player = 1 if board[i][j] == 'X' else -1 if board[i][j] == 'O' else 0
            rows[i] += player
            columns[j] += player
            if i == j:
                diag += player
            if i == n - j - 1:
                anti_diag += player

    winner = max(rows + columns + [diag, anti_diag], key=abs)
    if winner == n:
        return 'X'
    elif winner == -n:
        return 'O'
    else:
        return 'Ничья'

# Чтение доски
board = [list(input().strip()) for _ in range(3)]

# Определение победителя
winner = check_winner(board)

# Вывод результата
print(winner)

