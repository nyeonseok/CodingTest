alpha = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], [
    'M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

time = 0

input_alpha = list(input())


for i in range(len(input_alpha)):
    for j in range(len(alpha)):
        if input_alpha[i] in alpha[j]:
            time += j+3



print(time)
