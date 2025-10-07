import math

def solution(progresses, speeds):
    production = [0] * len(progresses)
    answer = []
    
    for i in range(len(progresses)):
        production[i] = math.ceil((100 - progresses[i]) / speeds[i])
    
    
    i = 0
    while 1 :
        cnt = 1
        if i == len(progresses) - 1:
            answer.append(cnt)
            break
        for j in range (i + 1, len(progresses)):
            if production[i] >= production[j]: 
                cnt += 1
                if j == len(progresses) - 1:
                    answer.append(cnt)
                    return answer             
                continue
            i = j
            break
        answer.append(cnt)
        
            
            

    return answer