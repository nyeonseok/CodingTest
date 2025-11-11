import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    li = list(map(int, sys.stdin.readline().strip()))
    graph.append(li)


def bfs(a, b):
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= a and 0 <= ny <= b:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return visited[a][b]


result = bfs(n - 1, m - 1)
print(result)
