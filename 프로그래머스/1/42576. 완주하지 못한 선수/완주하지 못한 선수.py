def solution(participant, completion):
    result = dict()
    
    for name in participant:
        if name not in result:
            result[name] = 1
        else:
            result[name] +=1
    
    for cpName in completion:
        result[cpName] -= 1
    
    answer = ''
    for key, value in result.items():
        if value > 0:
            answer = key
    return answer