def print_solution(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print("\n")


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens_util(board, row, n):
    if row >= n:
        print_solution(board)
        return True
    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solve_n_queens_util(board, row + 1, n) or res
            board[row][col] = 0
    return res


def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_util(board, 0, n):
        print("No solution exists.")
    else:
        print("All possible solutions are displayed above.")


n = 4
solve_n_queens(n)
