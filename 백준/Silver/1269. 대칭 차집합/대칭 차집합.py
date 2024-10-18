import sys

a, b = map(int, sys.stdin.readline().strip().split())

A = dict()
B = dict()

lA = list(map(int, sys.stdin.readline().strip().split()))
lB = list(map(int, sys.stdin.readline().strip().split()))


for a in lA:
    if a not in A:
        A[a] = 1

for b in lB:
    if b not in B:
        B[b] = 1

# A-B
for a, cnt in A.items():
    if a in B:
        A[a] = 0
    else:
        continue

# B-A
for b, cnt in B.items():
    if b in A:
        B[b] = 0
    else:
        continue

resultA = [a for a in A if A[a] == 1]
resultB = [b for b in B if B[b] == 1]

result = resultA + resultB
print(len(result))