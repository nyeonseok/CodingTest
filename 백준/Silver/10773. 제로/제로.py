import sys
from collections import deque
stack=deque()

k=int(sys.stdin.readline().strip())
for _ in range(k):
    a=int(sys.stdin.readline().strip())
    if a!=0:
        stack.append(a)
    else:
        stack.pop()
print(sum(stack))