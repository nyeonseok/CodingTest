import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().strip().split()))

a.sort()

def binary_search(arr1, target):
    left = 0
    right = len(arr1)-1
    while left <= right:
        mid = (left + right)//2
        if target == arr1[mid]:
            return 1
        elif target < arr1[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return 0

for i in range(m):
    if binary_search(a, b[i]):
        print(1)
    else:
        print(0)