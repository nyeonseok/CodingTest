import sys

n,m=map(int, sys.stdin.readline().strip().split())

poketmon=dict()
target=[]

for i in range(1, n+1):
    poketmon[i]=sys.stdin.readline().strip()
reversePoketmon = {v : k for k,v in poketmon.items()}

for j in range(m):
    target.append(sys.stdin.readline().strip())

for t in target:
    if t.isdigit():
        print(poketmon[int(t)])
    else:
        print(reversePoketmon[t])