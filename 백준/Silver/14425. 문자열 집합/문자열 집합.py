import sys

a,b=map(int,sys.stdin.readline().strip().split())


num=[]
for _ in range(a):
    num.append(sys.stdin.readline().strip())

sum=0
for _ in range(b):
    target = sys.stdin.readline().strip()
    if target in num:
        sum+=1
    else:
        continue
print(sum)