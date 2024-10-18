import sys
import math

n = int(sys.stdin.readline().strip())



for _ in range(n):
    a,b=map(int,sys.stdin.readline().strip().split())
    print(math.lcm(a,b))

