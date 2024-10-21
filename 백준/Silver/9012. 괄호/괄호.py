import sys
from collections import deque




def VPS(arr):
    stack = deque()
    for i in arr:
        if i == '(':
            stack.append(i)
        else:
            if not stack or stack[-1] == ')':
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


k = int(sys.stdin.readline().strip())
for _ in range(k):
    test = list(sys.stdin.readline().strip())
    if VPS(test):
        print("YES")
    else:
        print("NO")
