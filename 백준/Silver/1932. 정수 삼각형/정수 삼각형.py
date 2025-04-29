import sys

n = int(sys.stdin.readline())
triangle = []
dp = [[-1] * n for _ in range(n)]

for i in range(n):
    t = list(map(int, sys.stdin.readline().strip().split()))
    triangle.append(t)


def findMax(triangle, row, col, n, dp):
    if row == n:
        return 0
    if dp[row][col] != -1:
        return dp[row][col]

    maxNum = float("-inf")
    for i in range(col, col + 2):
        if i <= n:
            num = findMax(triangle, row + 1, i, n, dp)
            maxNum = max(num, maxNum)
    dp[row][col] = triangle[row][col] + maxNum
    return dp[row][col]


print(findMax(triangle, 0, 0, n, dp))
