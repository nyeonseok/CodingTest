import sys
from collections import deque

deck = deque()

n = int(sys.stdin.readline().strip())

for _ in range(n):
    command = list(sys.stdin.readline().strip().split())
    if len(command)==2:
        if command[0] == '1':
            deck.appendleft(int(command[1]))
        else:
            deck.append(int(command[1]))
    else:
        if command[0]=='3':
            if len(deck)>0:
                print(deck[0])
                deck.popleft()
            else:
                print(-1)
        elif command[0]=='4':
            if len(deck)>0:
                print(deck[-1])
                deck.pop()
            else:
                print(-1)
        elif command[0]=='5':
            print(len(deck))
        elif command[0]=='6':
            if len(deck)==0:
                print(1)
            else:
                print(0)
        elif command[0]=='7':
            if len(deck)>0:
                print(deck[0])
            else:
                print(-1)
        else:
            if len(deck)>0:
                print(deck[-1])
            else:
                print(-1)