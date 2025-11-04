import sys

n, k = map(int, sys.stdin.readline().split())
items = []
dp = [0] * (k + 1)

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    items.append([w, v])

for w, v in items:
    for i in range(k, w - 1, -1):
        if i >= w:
            dp[i] = max(dp[i], dp[i - w] + v)

print(dp[k])
