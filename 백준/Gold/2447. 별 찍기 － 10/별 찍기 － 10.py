def draw_star(x, y, n):
    if n == 1:
        stars[x][y] = "*"
        return

    div = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                # 가운데면 공백 처리
                continue
            draw_star(x + i * div, y + j * div, div)


N = int(input())
stars = [[" " for _ in range(N)] for _ in range(N)]

draw_star(0, 0, N)

for row in stars:
    print("".join(row))
