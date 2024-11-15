import sys

n=int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip().split()))

num.sort()

print(num[0]*num[-1])