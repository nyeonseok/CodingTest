import sys

t = int(sys.stdin.readline())

people = [[0 for _ in range(15)] for _ in range(15)]

for i in range(1, 15):
    people[0][i] = i

for i in range(1, 15):
    hap = 0
    for j in range(1, 15):
        hap += people[i - 1][j]
        people[i][j] = hap


for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(people[k][n])
