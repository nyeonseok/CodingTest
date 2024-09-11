n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

d = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
shark = []


def bfs():
    while shark:
        r, c = shark.pop(0)
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if not graph[nr][nc] or (graph[nr][nc] > graph[r][c] + 1):
                # 새로운 지점의 거리 정보 업데이트
                graph[nr][nc] = graph[r][c] + 1
                # 새로운 지점의 좌표 삽입
                shark.append((nr, nc))


for r in range(n):
    for c in range(m):
        if graph[r][c]:
            shark.append((r, c))
bfs()



print(max(map(max, graph))-1)
