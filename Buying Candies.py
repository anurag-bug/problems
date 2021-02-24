Buying Candies
Problem Description

Rishik likes candies a lot. So, he went to a candy-shop to buy candies.

The shopkeeper showed him N packets each containg A[i] candies for cost of C[i] nibbles, each candy in that packet has a sweetness B[i]. 
The shopkeeper puts the condition that Rishik can buy as many complete candy-packets as he wants but he can't buy a part of the packet.

Rishik has D nibbles, can you tell him the maximum amount of sweetness he can get from candy-packets he will buy?

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        dp = [[0 for _ in range(D+1)] for _ in range(0,len(A))]
        # sweetness = []
        for i in range(0,len(A)):
            for j in range(0,D+1):
                x = 0
                #check cost doesn't go below zero
                if j-C[i] >-1:
                    #Accept current packet
                    #but don't decrese i as we may inlude another ith packet
                    x = B[i]*A[i]+dp[i][j-C[i]]
                dp[i][j] = max(x,dp[i-1][j]) # dp[i-1][j] reject ith packet /(i-1 will become -1 in case of 0th row but won't cause any issue)
        # print(dp)
        return dp[len(A)-1][D]
