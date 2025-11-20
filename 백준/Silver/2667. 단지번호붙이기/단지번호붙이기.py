import sys

n = int(sys.stdin.readline())
maps = []
visited = [[False] * n for _ in range(n)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
apt = []

for _ in range(n):
    li = list(map(int, sys.stdin.readline().strip()))
    maps.append(li)


def dfs(x, y):
    visited[x][y] = True
    cnt = 1
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == 1 and visited[nx][ny] == False:
                cnt += dfs(nx, ny)
    return cnt


for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and visited[i][j] == False:
            answer = dfs(i, j)
            apt.append(answer)

print(len(apt))
apt.sort()
print("\n".join(map(str, apt)))
