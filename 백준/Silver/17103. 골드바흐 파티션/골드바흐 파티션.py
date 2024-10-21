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


def prime_table(limit):
    table = [False]*(limit+1)
    table[2] = True
    for i in range(3, len(table)+1, 2):
        if isprime(i):
            table[i] = True
    return table


def partition_cnt(x, table):
    cnt = 0
    if table[2] and table[x - 2]:  
        cnt += 1
    for i in range(3, x//2 + 1, 2):
        if table[i] and table[x-i]:
            cnt += 1
    return cnt


n = int(sys.stdin.readline().strip())
table=prime_table(1000000)

for _ in range(n):
    a = int(sys.stdin.readline().strip())
    print(partition_cnt(a, table))
