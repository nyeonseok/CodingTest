import sys

n = int(sys.stdin.readline())

people = []

for _ in range(n):
    kg, cm = map(int, sys.stdin.readline().strip().split())
    people.append((kg, cm))

rank = []

for i in range(n):
    cnt = 0
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    rank.append(cnt + 1)

[print(ranking, end=" ") for ranking in rank]
