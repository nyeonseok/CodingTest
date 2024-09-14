word = list(map(str, input()))

alphabet = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd'], ['E', 'e'], ['F', 'f'], ['G', 'g'], ['H', 'h'], ['I', 'i'], ['J', 'j'], ['K', 'k'], ['L', 'l'], [
    'M', 'm'], ['N', 'n'], ['O', 'o'], ['P', 'p'], ['Q', 'q'], ['R', 'r'], ['S', 's'], ['T', 't'], ['U', 'u'], ['V', 'v'], ['W', 'w'], ['X', 'x'], ['Y', 'y'], ['Z', 'z']]

b = [0]*26

for i in range(len(word)):
    for j in range(len(alphabet)):
        if word[i] in alphabet[j]:
            b[j] += 1

max_time = max(b)

cnt = 0
for i in range(len(b)):
    if max_time == b[i]:
        cnt += 1
if cnt > 1:
    print("?")
else:
    print(alphabet[b.index(max_time)][0])
