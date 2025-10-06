def solution(nums):
    nums.sort()
    count = dict()
    
    for num in nums:
        if num not in count.keys():
            count[num] = 1
        else:
            count[num] += 1
    
    if len(nums)/2 > len(count):
        answer = len(count)
    else:
        answer = len(nums)/2
        
    return answer