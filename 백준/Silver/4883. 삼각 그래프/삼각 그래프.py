# k 설정
k = 0

while True:
    
    # n 입력
    n = int(input())
    
    # 만약 n이 0이라면,
    if n == 0:
        # 테스트 종료
        break

    # n이 0이 아니라면, 진행
    else:
        
        # 테스트 번호 부여
        k += 1

        # grid 설계
        grid = [
            list(map(int, input().split())) for _ in range(n)
        ]

        # dp 설계
        dp = [
            [0] * 3 for _ in range(n)
        ]

        # dp 초기설정
        dp[0][1] = grid[0][1]
        dp[0][2] = dp[0][1] + grid[0][2]
        dp[1][0] = dp[0][1] + grid[1][0]
        dp[1][1] = min(dp[0][1], dp[0][2], dp[1][0]) + grid[1][1]
        dp[1][2] = min(dp[0][1], dp[0][2], dp[1][1]) + grid[1][2]

        # dp 채워넣기
        for i in range(2, n):
            dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + grid[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0]) + grid[i][1]
            dp[i][2] = min(dp[i-1][1], dp[i-1][2], dp[i][1]) + grid[i][2]
        
        # 출력
        print('%d. %d' % (k, dp[-1][1]))