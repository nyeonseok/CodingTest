alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# alpha = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], [
#     'M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

time = 0

input_alpha = list(input())



for i in range(len(input_alpha)):
    if 'A' <= input_alpha[i] <= 'C': time +=3
    elif 'D' <= input_alpha[i] <= 'F': time +=4
    elif 'G' <= input_alpha[i] <= 'I': time +=5
    elif 'J' <= input_alpha[i] <= 'L': time +=6
    elif 'M' <= input_alpha[i] <= 'O': time +=7
    elif 'P' <= input_alpha[i] <= 'S': time +=8
    elif 'T' <= input_alpha[i] <= 'V': time +=9
    else: time +=10


    


print(time)