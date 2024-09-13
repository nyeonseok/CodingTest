n = int(input())

for _ in range(n):
    b = list(input())
    print("%s%s" % (b[0], b[-1]))
    b = []*1000
