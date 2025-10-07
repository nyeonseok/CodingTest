from collections import deque

def solution(priorities, location):
    dq = deque(priorities)
    answer = 0
    
    while 1:
        if len(dq) == 0:
            break
        if location == 0 and dq[0] >= max(dq):
            return answer + 1
        if location == 0 and dq[0] < max(dq):
            location = len(dq) - 1
            dq.append(dq[0])
            dq.popleft()
            continue
        
        if dq[0] >= max(dq):
            answer += 1
            dq.popleft()
            location -= 1
            continue
        else:
            dq.append(dq[0])
            dq.popleft()
            location -= 1
    
    return answer