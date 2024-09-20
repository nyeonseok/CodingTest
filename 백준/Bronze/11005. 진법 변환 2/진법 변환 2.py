alpha = [['A', 10], ['B', 11], ['C', 12], ['D', 13], ['E', 14], ['F', 15], ['G', 16], ['H', 17], ['I', 18],['J', 19], ['K', 20], [
    'L', 21], ['M', 22], ['N', 23], ['O', 24], ['P', 25], ['Q', 26], ['R', 27], ['S', 28], ['T', 29], ['U', 30],['V', 31], ['W', 32],['X', 33], ['Y', 34],['Z', 35]]

a,b=map(int, input().split())
result=[]

while a/b!=0:
    if a%b >=10:
        for j in alpha:
            if a%b == j[1]:
                result.append(j[0])
                break
    else:
        result.append(int(a%b))
    a=int(a/b)

for i in range(len(result)):
    print(result[-1-i],end="")

