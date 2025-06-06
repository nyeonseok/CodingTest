import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().strip().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
