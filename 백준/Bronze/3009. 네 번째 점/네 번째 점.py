x = []
y = []

for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

# x 좌표 찾기
if x[0] == x[1]:
    findX = x[2]
elif x[0] == x[2]:
    findX = x[1]
else:
    findX = x[0]

# y 좌표 찾기
if y[0] == y[1]:
    findY = y[2]
elif y[0] == y[2]:
    findY = y[1]
else:
    findY = y[0]

print(findX, findY)
