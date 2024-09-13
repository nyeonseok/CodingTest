n = int(input())
b = list(map(int, input().split()))

max_num = max(b)
for i in range(n):
    b[i]=b[i]/max_num*100

sum=0
for i in range(n):
    sum=sum+b[i]

print(sum/n)