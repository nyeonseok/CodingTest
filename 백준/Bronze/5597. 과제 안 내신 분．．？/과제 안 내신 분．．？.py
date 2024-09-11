stds=[]
find=[]

for j in range(30):
    find.append(j+1)

for i in range(28):
    stds.append(int(input()))

for k in range(len(stds)):
    if stds[k] in find:
        find.remove(stds[k])

find.sort()
for i in range(len(find)):
    print(find[i])

