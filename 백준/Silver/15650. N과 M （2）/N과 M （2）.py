import sys

n, m = map(int, sys.stdin.readline().strip().split())
ans = []


def backTrack(start):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    for i in range(start, n + 1):
        if i not in ans:
            ans.append(i)
            backTrack(i + 1)
            ans.pop()


backTrack(1)
