No of ways to make change
def numberOfWaysToMakeChange(n, denoms):
    dp = [[0 if _ else 1 for _ in range(n+1)] for _ in range(len(denoms))]
    for j in range(n+1):
        for i in range(len(denoms)):
            if j-denoms[i] >= 0:
                dp[i][j] = dp[i][j-denoms[i]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
    
