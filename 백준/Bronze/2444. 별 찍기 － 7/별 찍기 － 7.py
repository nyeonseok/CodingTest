n = int(input())

time = 2*n-1
for i in range(1, time+1):
    if i < n:
        print(" "*(n-i) + "*"*(2*i-1))
    elif i==n: print("*"*(2*n-1))
    else:
        print(" "*(i-n) + "*"*(2*(2*n-i)-1))
