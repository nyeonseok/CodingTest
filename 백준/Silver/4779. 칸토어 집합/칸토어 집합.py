import sys


def cut(start, n):
    if n == 1:
        return
    for i in range(start+n//3, start+(n//3)*2):
        li[i] = ' '
    cut(start, n//3)
    cut(start+n//3*2, n//3)


while True:
    try:
        N = int(sys.stdin.readline().strip())
        li = ['-']*(3**N)
        cut(0, 3**N)
        print(''.join(li))
    except:
        break
