import sys

n, m = map(int, sys.stdin.readline().strip().split())

booly = dict()

for i in range(n+m):
    name = sys.stdin.readline().strip()
    if i < n:
        booly[name] = 1
    else:
        if name in booly:
            booly[name] -= 1
        else:
            continue

result = {key : booly[key] for key in sorted(booly)}


cnt = sum(1 for value in result.values() if value == 0)
print(cnt)

for name, count in result.items():
    if count == 0:
        print(name)
    else:
        continue
