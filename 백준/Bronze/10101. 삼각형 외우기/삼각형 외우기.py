a=int(input())
b=int(input())
c=int(input())

result = a + b + c

if a==60 and b==60 and c==60:
    print("Equilateral")
elif result==180 and (a==b or b==c or c==a):
    print("Isosceles")
elif result==180 and (a!=b and b!=c and c!=a):
    print("Scalene")
else:
    print("Error")