import sys
from collections import deque


def nice(arr):
    stack = deque()
    final = deque()
    pos = 1

    while stack or arr:
        if arr and arr[0]==pos:
            final.append(arr.pop(0))
            pos += 1
        elif stack and stack[-1]==pos:
            final.append(stack.pop())
            pos+=1
        elif arr:
            stack.append(arr.pop(0))
        else:
            return False
    return True
    


n = int(sys.stdin.readline().strip())

now = list(map(int, sys.stdin.readline().strip().split()))

if nice(now):
    print("Nice")
else:
    print("Sad")
