n=int(input())

if n%3==0 and n%5==0:
    print(n//5)

elif n%3==0 and n%5!=0:
    count=[]
    count.append(n//3)
    for i in range(1, n//5 + 1):
        if (n-5*i)%3==0:
            count.append((n-5*i)//3 + i)
    for i in range(1, n//3 + 1):
        if (n-3*i)%5==0:
            count.append((n-3*i)//5 + i)
    print(min(count))

elif n%5==0 and n%3!=0:
    count=[]
    count.append(n//5)
    for i in range(1, n//3 + 1):
        if (n-3*i)%5==0:
            count.append((n-3*i)//5 + i)
    for i in range(1, n//5 + 1):
        if (n-5*i)%3==0:
            count.append((n-5*i)//3 + i)
    print(min(count))

else:
    count=[]
    for i in range(1, n//3 + 1):
        if (n-3*i)%5==0:
            count.append((n-3*i)//5 + i)
    for i in range(1, n//5 + 1):
        if (n-5*i)%3==0:
            count.append((n-5*i)//3 + i)
    if count:
        print(min(count))
    else:
        print(-1)