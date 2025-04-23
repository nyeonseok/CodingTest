import sys
from collections import deque

n = int(sys.stdin.readline().strip())

stack = deque()

for _ in range(n):
    cmd = list(sys.stdin.readline().strip().split())

    if cmd[0] == "push":
        stack.append(cmd[-1])
    elif cmd[0] == "pop":
        if len(stack):
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(1) if len(stack) == 0 else print(0)
    else:
        print(stack[-1]) if len(stack) > 0 else print(-1)
