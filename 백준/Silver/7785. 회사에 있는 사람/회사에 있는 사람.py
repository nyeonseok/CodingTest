import sys

n= int(sys.stdin.readline())


In=dict()
for _ in range(n):
    a,b=sys.stdin.readline().strip().split()
    if b=='enter':
        In[a] = b
    elif b=='leave':
        del In[a]

now = sorted(In.keys(), reverse=True)

for i in now:
    print(i)