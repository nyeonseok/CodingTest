import sys

n = int(sys.stdin.readline())
S = []
N = []

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    S.append(row)
    N.append(i)

answer = float("inf")


def dfs(idx, start):
    global answer
    if len(start) == n // 2:
        link = [x for x in N if x not in start]
        start_sum = 0
        link_sum = 0
        for i in start:
            for j in start:
                start_sum += S[i][j]
        for i in link:
            for j in link:
                link_sum += S[i][j]
        diff = abs(start_sum - link_sum)
        answer = min(answer, diff)
        return answer

    for i in range(idx, n):

        start.append(i)
        dfs(i + 1, start)
        start.pop()


dfs(0, [])
print(answer)
