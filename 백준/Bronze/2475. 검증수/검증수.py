import sys

num=list(sys.stdin.readline().strip().split())

hap=0

for i in num:
    hap+=int(i)**2

print(hap%10)