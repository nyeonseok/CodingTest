
while True:
    length=[]
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    length.append(a)
    length.append(b)
    length.append(c)
    length.sort()
    if length[0] + length[1] <= length[2]:
        print("Invalid")
    elif length[0]==length[1] and length[1]==length[2]:
        print("Equilateral")
    elif length[0]!=length[1] and length[1]!=length[2] and length[2]!=length[0]:
        print("Scalene")
    else:
        print("Isosceles")