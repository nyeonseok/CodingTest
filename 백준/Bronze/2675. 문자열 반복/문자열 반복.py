t = int(input())
p = []

for _ in range(t):
    r, p = input().split()
    r = int(r)
    p = list(p)
    for i in p:
        print(i * r, end='')  # 줄바꿈 없이 출력
    print()  # 줄바꿈
