a=[[]*9 for _ in range(9)]


x,y=0,0
for i in range(9):
    a[i] = list(map(int, input().split()))

maxValue = a[0][0]
for i in range(9):
    for j in range(9):
        if maxValue < a[i][j]:
            maxValue = a[i][j]
            x,y=i,j
print(maxValue)
print(x+1,y+1)