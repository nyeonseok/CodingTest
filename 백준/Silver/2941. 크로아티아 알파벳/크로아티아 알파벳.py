c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
final = []

word = list(input())

i=0
while i<len(word):

    if i+2<len(word):
        if word[i]+word[i+1] in c or word[i]+word[i+1]+word[i+2] in c:
            final.append(word[i]+word[i+1] if word[i]+word[i+1] in c else word[i]+word[i+1]+word[i+2])
            i += 2 if word[i]+word[i+1]  in c else 3
        else:
            final.append(word[i])
            i+=1
    else:
        if i+1<len(word):
            if word[i] + word[i+1] in c:
                final.append(word[i]+word[i+1])
                i+=2
            else:
                final.append(word[i])
                i+=1
        else:
            final.append(word[i])
            i+=1
    

    
    
print(len(final))
