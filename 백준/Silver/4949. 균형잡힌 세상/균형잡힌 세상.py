import sys
from collections import deque


def goodStr(arr):
    stack = deque()
    for a in arr:
        if a == '(' or a == '[':
            stack.append(a)
        elif a.isalpha():
            continue
        else:
            if a == ')' and (len(stack) == 0 or stack[-1] != '('):
                return False
            if a == ']' and (len(stack) == 0 or stack[-1] != '['):
                return False
            if len(stack) > 0 and ((a == ')' and stack[-1] == '(')) or (a == ']' and stack[-1] == '['):
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


while True:
    string = list(sys.stdin.readline().rstrip('\n'))
    if string[0] == '.' and len(string) == 1:
        break
    strings = [item for item in string if item.strip()]
    if goodStr(strings):
        print("yes")
    else:
        print("no")
