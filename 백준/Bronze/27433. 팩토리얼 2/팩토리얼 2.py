import sys

n = int(sys.stdin.readline().strip())


def factorial(x):
    if x == 0:
        return 1
    result = x
    return result*factorial(x-1)


result = factorial(n)
print(result)
