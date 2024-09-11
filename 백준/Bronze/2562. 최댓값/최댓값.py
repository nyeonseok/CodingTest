nums=[]

for i in range(9):
    nums.append(int(input()))

max_value = max(nums)
for i in range(9):
    if nums[i] == max_value:
        print(f'{max_value}\n{i+1}')