a1, a0 = map(int,input().split())
c=int(input())
n0=int(input())

def result(n):
    return a1*n + a0 - c*n

goal=1
for i in range(n0,n0+101):
    if result(i)>0:
        goal=0
        print(0)
        break
if goal==1:
    print(1)