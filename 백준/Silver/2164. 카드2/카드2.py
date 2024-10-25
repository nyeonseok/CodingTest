import sys
from collections import deque

queue = deque()

n = int(sys.stdin.readline().strip())
queue.extend([x+1 for x in range(n)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue.popleft())