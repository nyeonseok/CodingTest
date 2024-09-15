n, m = map(int, input().split())
a = [[] for _ in range(n)]  # 각 행에 독립된 리스트 생성
b = [[] for _ in range(n)]  # 각 행에 독립된 리스트 생성
c = [[0]*m for _ in range(n)]  # n x m 크기의 2차원 배열 초기화 (모두 0으로 초기화)


for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(n):
    b[i] = list(map(int, input().split()))


for i in range(n):
    for j in range(m):
        c[i][j] = a[i][j] + b[i][j]

        

for i in range(n):
    for j in range(m):
        print(c[i][j], end=' ')
    print()
