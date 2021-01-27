Problem Description

Given a string A. Find the longest palindromic subsequence 
(A subsequence which does not need to be contiguous and is a palindrome).

You need to return the length of longest palindromic subsequence.

Approach: Similar to finding longest common subsequence b/w A and B
Reverse A and find longest common subsequence.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        B = A[::-1]
        n = len(A)
        m = len(B)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,n+1):
            for j in range(1, m+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max (dp[i][j-1], dp[i-1][j])
        return dp[n][m]
