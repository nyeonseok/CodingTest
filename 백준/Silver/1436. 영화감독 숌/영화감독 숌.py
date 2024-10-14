import sys

maxNum = sys.maxsize

n=int(input())

index=0

for i in range(666,maxNum):
    if str(i).count('666')>0:
        index+=1
        if index==n:
            print(i)
            break