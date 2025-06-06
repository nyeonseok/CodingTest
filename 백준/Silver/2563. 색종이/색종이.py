import sys
ground = [[False]*100 for _ in range(100)]
colors = []

n = int(sys.stdin.readline().strip())


for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    colors.append((a, b))


def search(ground, arr):
    for i in range(arr[0], arr[0]+10):
        for j in range(arr[1], arr[1]+10):
            if ground[i][j] == False:
                ground[i][j] = True
            else:
                continue
    return ground


for color in colors:
    ground = search(ground, color)

cnt = 0
cnt = sum(1 for i in range(100) for j in range(100) if ground[i][j] == True)

print(cnt)
