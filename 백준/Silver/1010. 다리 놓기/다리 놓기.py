import sys
import math

input = sys.stdin.readline().strip()

t=int(input)

for _ in range(t):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(math.comb(b,a))