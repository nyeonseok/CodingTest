import sys

n = int(input())
l1 = str(input())
cnt=[]

#오른쪽 R모음
result = l1.rstrip('R')
cnt.append(result.count('R'))

#오른쪽 B모음
result = l1.rstrip('B')
cnt.append(result.count('B'))

#오른쪽 R모음
result = l1.lstrip('R')
cnt.append(result.count('R'))

#오른쪽 B모음
result = l1.lstrip('B')
cnt.append(result.count('B'))

print(min(cnt))
