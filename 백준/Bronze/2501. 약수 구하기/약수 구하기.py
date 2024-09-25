a, b = map(int, input().split())

cnt = 0
for i in range(1, a+1):
    if a % i == 0:
        cnt += 1
    if cnt == b:
        print(i)
        break
if cnt < b:
    print(0)

