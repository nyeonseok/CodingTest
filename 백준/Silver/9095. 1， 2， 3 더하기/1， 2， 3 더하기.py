import sys

t = int(sys.stdin.readline())
dp = [0] * 12


dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])
