n =int(input())
scores=[int(input()) for _ in range(n)]

high_score=scores[-1]   #가장 마지막 레벨 점수를 최고 점수로 설정
cnt=0



for i in range(len(scores)-2, -1, -1):  #scores마지막에서 한칸 앞에 원소부터 역순으로 순회
    while scores[i]>=high_score:        #high_score보다 크거나 같으면 while실행
        scores[i]=scores[i]-1           #1씩 빼줌
        cnt+=1
    high_score=scores[i]                #작으면 high_score 갱신

print(cnt)
