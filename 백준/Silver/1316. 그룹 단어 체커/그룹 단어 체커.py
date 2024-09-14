n = int(input())

cnt = n
for _ in range(n):   
    word = list(input())
    b=['']*len(word)
    b[0] = word[0]
    bIndex = 1
    for i in range(1, len(word)):
        if word[i-1] != word[i] and word[i] not in b:
            b[bIndex] = word[i]
        elif word[i-1] != word[i] and word[i] in b:
            cnt -= 1
            break
        elif word[i-1] == word[i]:
            continue
        bIndex += 1

print(cnt)
