import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

rgb = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dp = [[-1] * 3 for _ in range(n)]


def price(rgb, row, col, n, dp):
    if row == n:
        return 0
    if dp[row][col] != -1:
        return dp[row][col]

    minCost = float("inf")
    for i in range(3):
        if i == col:
            continue
        cost = price(rgb, row + 1, i, n, dp)
        minCost = min(minCost, cost)

    dp[row][col] = rgb[row][col] + minCost
    return dp[row][col]


result = min(price(rgb, 0, 0, n, dp), price(rgb, 0, 1, n, dp), price(rgb, 0, 2, n, dp))

print(result)
