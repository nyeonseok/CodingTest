import sys

n=int(sys.stdin.readline().strip())

num = list(map(int,input().split()))

arr=sorted(list(set(num)))

dic = {arr[i] : i for i in range(len(arr))}

for i in num:
    print(dic[i], end=' ')