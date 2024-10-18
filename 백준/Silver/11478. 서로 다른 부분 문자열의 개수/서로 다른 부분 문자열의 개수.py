import sys

string = list(sys.stdin.readline().strip())

cnt = dict()

for i in range(len(string)):
    for j in range(i, len(string)+1):
        slicing = ''.join(string[i:j])
        if slicing not in cnt:
            cnt[slicing] = 1
        else:
            cnt[slicing] += 1
        slicing = ''

del cnt['']
print(len(cnt))
