import sys
import math

def isprime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

n = int(sys.stdin.readline().strip())
for _ in range(n):
    a = int(sys.stdin.readline().strip())
    while True:
        if isprime(a):
            print(a)
            break
        a += 1
