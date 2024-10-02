n = int(input())
num = list(map(int, input().split()))
x = int(input())

num.sort()

cnt = 0
left,right=0, n-1

while left < right:
    if num[left]+num[right] < x:
        left+=1
    elif num[left]+num[right] == x:
        cnt += 1
        left+=1
    else:
        right-=1
        
print(cnt)
