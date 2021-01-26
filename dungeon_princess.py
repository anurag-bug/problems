Dungeon Princess
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Given a 2D array of integers A of size M x N. Find and return the knight's minimum initial health so that he is able to rescue the princess.




class Solution:
	# @param A : list of list of integers
	# @return an integer
	def calculateMinimumHP(self, A):
	    rows = len(A)
	    cols = len(A[0])
	   # each dp cell represents energy required to reach current cell
	    dp = [[0 for _ in range(cols)]for _ in range(rows)]
	   # top down approach
	   # start with the bottom right cell assuming knight reaches there with 0 energy.
	    for i in range(rows-1, -1, -1):
	        for j in range(cols-1, -1, -1):
	           # corner cases
                if i == rows-1 and j == cols-1:
                    # select 0 if energy req is negative
                    dp[i][j] = max(0 - A[i][j], 0)
                elif i == rows-1:
                    dp[i][j] = max(0, dp[i][j+1] - A[i][j])
                elif j == cols -1:
                    dp[i][j] = max(0, dp[i+1][j] - A[i][j])
                # normal case
                else:
                    minReq = min(dp[i][j+1], dp[i+1][j])
                    dp[i][j] = max(minReq - A[i][j], 0)
	    return dp[0][0]+1
