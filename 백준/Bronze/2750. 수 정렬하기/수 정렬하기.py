n=int(input())
num=[]
for _ in range(n):
    num.append(int(input()))

num.sort()
for n in num:
    print(n)