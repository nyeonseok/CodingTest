m=int(input())
n=int(input())


prime=[]

for i in range(m,n+1):
    prime.append(i)

for i in range(m, n+1):
    if i==1:
        prime.pop(prime.index(i))
        continue
    
    for j in range(2, i):
        if i%j==0:
            prime.pop(prime.index(i))
            break


if len(prime)==0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))