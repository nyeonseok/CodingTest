n = int(input())  # 입력받을 줄의 수
h = [int(input()) for _ in range(n)]  # 각 줄의 숫자를 정수로 변환하여 리스트에 저장

stack = []
result = 0

for i in h:
    while stack and stack[-1] <= i:
        stack.pop()
    stack.append(i)
    result += len(stack)-1


print(result)  # 결과 출력
