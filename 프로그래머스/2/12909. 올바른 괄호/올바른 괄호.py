def solution(s):
    answer = True
    
    keep = []
    
    for i in s:
        if len(keep) == 0:
            keep.append(i)
            continue
        if keep[-1] == "(" and i == ")":
            keep.pop()
        else:
            keep.append(i)
    
    if len(keep) != 0:
        answer = False

    return answer