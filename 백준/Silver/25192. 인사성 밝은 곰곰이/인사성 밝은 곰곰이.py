import sys

n = int(sys.stdin.readline().strip())

cnt = 0
for _ in range(n):
    str1 = sys.stdin.readline().strip()
    if str1 == 'ENTER':
        name = dict()
    else:
        if str1 not in name:
            name[str1] = 1
            cnt += 1
        else:
            continue
    
print(cnt)
