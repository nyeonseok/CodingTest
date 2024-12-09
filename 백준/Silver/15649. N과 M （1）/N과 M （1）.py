import sys

n, m = map(int, sys.stdin.readline().strip().split())
ans = []


def backTrack():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    for i in range(1, n + 1):
        if i not in ans:
            ans.append(i)
            backTrack()
            ans.pop()


backTrack()
