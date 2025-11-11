import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


DFSvisted = []
stack = []


def dfs(v):
    stack.append(v)

    while stack:
        node = stack.pop()
        if node not in DFSvisted:
            DFSvisted.append(node)
            for neighbor in reversed(sorted(graph[node])):
                stack.append(neighbor)


BFSvisted = []
queue = deque()


def bfs(v):
    queue.append(v)

    while queue:
        node = queue.popleft()
        if node not in BFSvisted:
            BFSvisted.append(node)
            for neighbor in sorted(graph[node]):
                queue.append(neighbor)


dfs(v)
bfs(v)

for i in range(len(DFSvisted)):
    print(DFSvisted[i], end=" ")
print()
for i in range(len(BFSvisted)):
    print(BFSvisted[i], end=" ")
