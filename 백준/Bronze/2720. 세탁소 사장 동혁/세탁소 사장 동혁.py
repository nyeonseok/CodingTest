import sys

money = [25, 10, 5, 1]


t = int(input())
n = [sys.stdin.readline() for _ in range(t)]
n = [int(line.strip()) for line in n]

result = [[0, 0, 0, 0] for _ in range(t)]

for i in range (t):
    for j in range(4):
        result[i][j] = int(n[i]/money[j])
        n[i] %= money[j]

for i in range(t):
    print(result[i][0], result[i][1], result[i][2], result[i][3])

