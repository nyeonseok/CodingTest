nums = []
diff = [] * 10
cnt = 1

for i in range(10):
    nums.append(int(input()))

for i in range(10):
    nums[i] = nums[i] % 42
    
diff.append(nums[0])

for i in range(1, 10):
    for j in range(i+1, 10):
        if nums[i] != nums[j] and nums[i] not in diff:
            diff.append(nums[i])
        if nums[-1] not in diff:
            diff.append(nums[-1])

print(len(diff))