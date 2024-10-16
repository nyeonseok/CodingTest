import sys

n=int(sys.stdin.readline().strip())



numA=[]
numB=[]

for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    numA.append(a)
    numB.append(b)

sortArr=sorted(zip(numA,numB))

for i in range(n):
    print(sortArr[i][0], sortArr[i][1])