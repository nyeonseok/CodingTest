grades = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
total = [list(input().split()) for _ in range(20)]


sum = 0.0
hak_sum =0.0
for i in range(20):
    if total[i][2] != 'P':
        sum += grades[total[i][2]] * float(total[i][1])
        hak_sum += float(total[i][1])
    else:
        continue
print(sum/hak_sum)