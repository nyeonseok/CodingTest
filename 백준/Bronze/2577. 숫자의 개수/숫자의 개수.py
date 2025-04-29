import sys

gop = 1
count = [0] * 10

for _ in range(3):
    a = int(sys.stdin.readline())
    gop *= a


for n in str(gop):
    count[int(n)] += 1


for i in count:
    print(i)
