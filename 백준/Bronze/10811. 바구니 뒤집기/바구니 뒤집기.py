n, m = map(int, input().split())
b = []*n

for n in range(1, n + 1):
    b.append(n)

for _ in range(m):
    i, j = map(int, input().split())
    pos = i-1
    for k in range(j-1, i-2, -1):

        temp = b[k]
        b[k] = b[pos]
        b[pos] = temp
        pos += 1
        if pos == k or pos > k:
            break


for i in range(n):
    print(b[i], end=' ')
