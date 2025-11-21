import sys

n = int(sys.stdin.readline())
dump=[]
rank=[]

for _ in range(n):
    x,y =list(map(int, sys.stdin.readline().split()))
    dump.append((x,y))

while len(rank)<n:
    for i in range(n):
        ranking = 1
        ix,iy = dump[i]
        for j in range(n):
            if i==j:
                continue
            jx,jy = dump[j]
            if jx>ix and jy>iy:
                ranking+=1
        rank.append(ranking)

print(' '.join(map(str,rank)))