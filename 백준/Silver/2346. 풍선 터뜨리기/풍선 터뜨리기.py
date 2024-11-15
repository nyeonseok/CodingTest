import sys
from collections import deque

n = int(sys.stdin.readline().strip())
num = deque(enumerate(map(int, sys.stdin.readline().strip().split())))

while num:
    idx, move = num.popleft()
    print(idx+1, end=" ")
    if move>0:
        num.rotate(-(move-1))
    else:
        num.rotate(-move)