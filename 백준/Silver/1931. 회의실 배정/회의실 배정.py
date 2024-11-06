import sys


n = int(sys.stdin.readline().strip())
schedule = []
min = sys.maxsize - 1
for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    schedule.append((a, b))


schedule = sorted(schedule, key=lambda x: (x[1], x[0]))
cnt=0
endPoint=0

for start, end in schedule:
    if start>=endPoint:
        cnt+=1
        endPoint=end
print(cnt)
