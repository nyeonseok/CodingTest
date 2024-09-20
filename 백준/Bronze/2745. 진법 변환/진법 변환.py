alpha = [['A', 10], ['B', 11], ['C', 12], ['D', 13], ['E', 14], ['F', 15], ['G', 16], ['H', 17], ['I', 18],['J', 19], ['K', 20], [
    'L', 21], ['M', 22], ['N', 23], ['O', 24], ['P', 25], ['Q', 26], ['R', 27], ['S', 28], ['T', 29], ['U', 30],['V', 31], ['W', 32],['X', 33], ['Y', 34],['Z', 35]]

input_list, b = input().split()
input_list = list(map(str, input_list))
b = int(b)

result = [0] * len(input_list)


for i in range(len(input_list)):
    result[i] = b**(len(input_list)-i-1)



for i in range(len(input_list)):   
    if input_list[i].isdigit():
        result[i] *= int(input_list[i])
    else:
        for j in alpha:
            if input_list[i] == j[0]:
                result[i] *= j[1]
print(sum(result))

