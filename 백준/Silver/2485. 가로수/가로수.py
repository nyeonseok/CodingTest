import sys
import math

n = int(sys.stdin.readline().strip())

tree = [0]*n

for i in range(n):
    tree[i] = int(sys.stdin.readline().strip())

diff = [0]*(n-1)
for i in range(n-1):
    diff[i] = tree[i+1]-tree[i]

gcd = diff[0]
for d in range(1, len(diff)):
    gcd = math.gcd(gcd, diff[d])


cnt = len(tree)-2
maxCnt = (tree[-1]-tree[0])//gcd - 1
cnt = maxCnt-cnt

print(cnt)
