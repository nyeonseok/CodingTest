n, m = map(int, input().split())
b = [0] * n

for i in range(n):
    b[i] = i+1

temp = 0
for m in range(m):
    i, j = map(int, input().split())
    temp = b[i-1]
    b[i-1] = b[j-1]
    b[j-1] = temp

for i in range(n):
    print(b[i], end=' ')
