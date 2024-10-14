n,k=map(int,input().split())

scores=list(map(int,input().split()))

scores.sort()

print(scores[-1*k])