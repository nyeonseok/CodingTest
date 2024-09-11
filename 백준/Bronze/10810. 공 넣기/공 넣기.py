n, m = map(int, input().split())
b = [0]*n

for m in range(m):
    i, j, k = map(int, input().split())
    for index in range(i-1,j):
        b[index]=k

for i in range(n):
    print(b[i], end=' ')
