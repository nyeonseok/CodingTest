import sys

n=int(sys.stdin.readline().strip())
count=dict()

li = list(map(int, sys.stdin.readline().strip().split()))

m=int(sys.stdin.readline().strip())

target=list(map(int, sys.stdin.readline().strip().split()))




for l in li:
    if l not in count:
        count[l] = 1
    else:
        count[l] += 1

for i in target:
    if i not in count:
        print(0, end=" ")
    else:
        print(count[i], end=" ")