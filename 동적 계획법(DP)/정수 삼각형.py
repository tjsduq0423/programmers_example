def solution(tri):
    dp = [[0] * len(i) for i in tri]
    dp[0][0] = tri[0][0]

    for i in range(len(tri) - 1):
        for j in range(i + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + tri[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + tri[i + 1][j + 1])
    print(dp)
    return max(dp[-1])


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
