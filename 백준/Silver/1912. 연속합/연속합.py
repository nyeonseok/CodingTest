import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

dp = [0] * n

dp[0] = arr[0]

for i in range(1, n):
    hap = dp[i - 1] + arr[i]

    if arr[i] < hap:
        dp[i] = hap
    else:
        dp[i] = arr[i]

print(max(dp))
