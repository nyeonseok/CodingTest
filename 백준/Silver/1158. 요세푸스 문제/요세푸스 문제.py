import sys

n, m = map(int, sys.stdin.readline().strip().split())

number = [i for i in range(1, n + 1)]
remove = []
num = 0

for _ in range(n):
    num += m - 1
    num = num % len(number) if num >= len(number) else num
    remove.append(number.pop(num))

print("<", end="")
for i in range(len(remove) - 1):
    print(remove[i], end=", ")
print(remove[-1], end=">")
