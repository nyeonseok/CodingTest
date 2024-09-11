n, w, L = map(int, input().split())
q = list(map(int, input().split()))

length = [0]*w
time = 0

while length:
    time+=1
    length.pop(0)
    if q:
        if sum(length) + q[0] <= L:
            length.append(q.pop(0))
        else:
            length.append(0)
print(time)
