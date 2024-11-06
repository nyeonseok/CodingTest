import sys


queue = list()
n, k = map(int, sys.stdin.readline().strip().split())

for i in range(1, n+1):
    queue.append(i)


cnt = 0
print("<", end="")
while queue:
    for i in range(k-1):
        queue.append(queue[i])
    for i in range(k-1):
        queue.pop(0)
    cnt += 1
    if cnt == n:
        print(queue[0], end="")
    else:
        print(queue[0], end=', ')
    queue.pop(0)
print(">")
