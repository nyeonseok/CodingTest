import sys

n = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

total = 0

for i in range(n):
    cnt1 = 0
    bInclude = students[i] - b
    cnt1 += 1
    if bInclude > 0:
        if bInclude % c == 0:
            cnt1 += bInclude // c
        else:
            cnt1 += (bInclude // c) + 1
    total += cnt1
print(total)