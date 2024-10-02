import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited_cnt = [0]*(n+1)


def bfs(node):
    q = deque()
    q.append(node)
    visited_cnt[node] = 1
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited_cnt[i] == 0:
                visited_cnt[i] = visited_cnt[node] + 1
                q.append(i)



bfs(1)
max_num = max(visited_cnt)

print(visited_cnt.index(max_num),max_num-1,visited_cnt.count(max_num))