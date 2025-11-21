import sys

sys.setrecursionlimit(10**6)
t = int(sys.stdin.readline())


def dfs(start, end):
    visited[end][start] = True
    cnt = 1
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dy, dx in direction:
        nx = start + dx
        ny = end + dy
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 1 and visited[ny][nx] == False:
                cnt += dfs(nx, ny)
    return cnt


li = []
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == False:
                answer = dfs(j, i)
                li.append(answer)
    print(len(li))
    li = []
