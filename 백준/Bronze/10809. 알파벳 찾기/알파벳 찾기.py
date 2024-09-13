S=list(map(str,input()))

result=[-1]*26

alpha=[]*26
for a in range(97,123):
    alpha.append(chr(a))


for a in alpha:
    if a in S:
        result[alpha.index(a)]=S.index(a)

for i in range(len(result)):
    print(result[i],end=' ')

