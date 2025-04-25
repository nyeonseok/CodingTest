import sys

n = int(sys.stdin.readline())
value = n

cnt = 0
while True:
    if n == 0:
        cnt += 1
        break
    elif n < 10:
        n = 10 * n + n
        cnt += 1
    else:
        hap = n // 10 + n % 10
        n = 10 * (n % 10) + hap % 10
        cnt += 1
    if n == value:
        break

print(cnt)
