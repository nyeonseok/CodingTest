import sys

n = int(sys.stdin.readline())
boards = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    boards.append(row)


def rotate_90(board):
    rotate = list(zip(*board[::-1]))
    return rotate


def rotate_180(board):
    rotate = [row[::-1] for row in board[::-1]]
    return rotate


def rotate_minus_90(board):
    rotate = list(zip(*board))[::-1]
    return rotate


def move_left(board):
    new_board = []
    for i in range(n):
        new_row = []
        for j in range(n):
            if board[i][j] != 0:
                new_row.append(board[i][j])
        r = 0
        while r < len(new_row) - 1:
            if new_row[r] == new_row[r + 1]:
                new_row[r] *= 2
                new_row.pop(r + 1)
                r += 1
            else:
                r += 1
        new_row += [0] * (n - len(new_row))
        new_board.append(new_row)
    return new_board


def move(board, direction):
    # 위
    if direction == 0:
        top = rotate_minus_90(board)
        moved = move_left(top)
        result = rotate_90(moved)
        return result
    # 오른쪽
    elif direction == 1:
        right = rotate_180(board)
        moved = move_left(right)
        result = rotate_180(moved)
        return result
    # 아래
    elif direction == 2:
        bottom = rotate_90(board)
        moved = move_left(bottom)
        result = rotate_minus_90(moved)
        return result
    # 왼쪽
    else:
        moved = move_left(board)
        return moved


answer = 0


def dfs(board, depth):
    global answer
    if depth == 5:
        answer = max(answer, max(map(max, board)))
        return

    for direction in range(4):
        new_board = move(board, direction)
        dfs(new_board, depth + 1)


dfs(boards, 0)
print(answer)
