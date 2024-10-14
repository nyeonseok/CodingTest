m, n = map(int, input().split())

cheseu = []

count = []


answer = [[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]]


def countDiff(arr1, arr2):
    diff = sum(1 for x, y in zip(arr1, arr2) if x != y)
    return diff

for _ in range(m):
    cheseu.append(list(input()))

cheseu = [[0 if ch == 'W' else 1 for ch in row] for row in cheseu]


for i in range(m-7):
    for j in range(n-7):
        cnt1 = 0
        cnt2 = 0    
        matrix = []   
        for k in range(8):
            matrix.append(cheseu[i+k][j:j+8])
        for l in range(8):
            cnt1+=countDiff(matrix[l], (answer[0] if (l==0 or l%2==0) else answer[1]))
            cnt2+=countDiff(matrix[l], (answer[1] if (l==0 or l%2==0) else answer[0]))

        count.append(min(cnt1, cnt2))    
print(min(count))