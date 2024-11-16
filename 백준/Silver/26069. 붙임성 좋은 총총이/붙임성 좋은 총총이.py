import sys

dance = {"ChongChong": 1}

n = int(sys.stdin.readline().strip())

for _ in range(n):
    a, b = map(str, sys.stdin.readline().strip().split())
    if a in dance:
        dance[b]=1
    if b in dance:
        dance[a]=1

print(len(dance))