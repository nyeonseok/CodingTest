people = int(input())
time = list(map(int, input().split()))
tTime = [0]*people

time.sort()
total=0

for i in range(people):
    total = total + time[i]
    tTime[i]=total
print(sum(tTime))