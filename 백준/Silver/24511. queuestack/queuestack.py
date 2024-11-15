import sys
from collections import deque

n = int(sys.stdin.readline().strip())
queuestack = deque(map(int, sys.stdin.readline().strip().split()))
elements = deque(map(int, sys.stdin.readline().strip().split()))

k = int(sys.stdin.readline().strip())
push = list(map(int, sys.stdin.readline().strip().split()))


cnt = queuestack.count(0)
result = zip(queuestack, elements)
result = sorted(result, key=lambda x: x[0])

# print(result)

if cnt>0:
    result=result[:cnt]

zero, number=zip(*result)
# print(number)
if cnt>0:
    if k<cnt:
        for i in range(len(number)-1,cnt-k-1,-1):
            print(number[i], end=" ")
    elif k==cnt:
        for i in range(len(number)-1,-1,-1):
            print(number[i], end=" ")
    else:
        for i in range(len(number)-1,-1,-1):
            print(number[i], end=" ")
        for i in range(k-cnt):
            print(push[i], end=" ")
else:
    for i in range(k):
        print(push[i], end=" ")
