import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
stack = []
visited = []

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    stack.append(node)

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for linked in graph[v]:
                stack.append(linked)


dfs(1)
print(len(visited) - 1)
