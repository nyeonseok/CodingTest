import sys
import math

n, k = map(int,sys.stdin.readline().strip().split())
print(math.comb(n,k))