import sys

n = int(sys.stdin.readline())

score = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    score[i] = int(sys.stdin.readline())

dp[1] = score[1]
if n >= 2:
    dp[2] = score[1] + score[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + score[i], dp[i - 3] + score[i - 1] + score[i])

print(dp[-1])
