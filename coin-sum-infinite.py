Coin Sum Infinite

You are given a set of coins A. In how many ways can you make sum B assuming you 
have infinite amount of each coin in the set.

NOTE:
Coins in set A will be unique. Expected space complexity of this problem is O(B).
The answer can overflow. So, return the answer % (106 + 7).

# Top Down Approach with Memoization (Memory Limit Exceeded)
import sys
sys.setrecursionlimit(999999999)
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B, mydict = {}):
	    if (tuple(A), B) in mydict:
	        return mydict[(tuple(A), B)]
	    if B == 0:
	        return 1
	    if len(A) == 0:
	        return 0
	    if B < 0:
	        return 0
	    else:
	        x = self.coinchange2(A[0:-1], B) + self.coinchange2(A, B-A[-1])
	        mydict[(tuple(A), B)] = x % 1000007
	        return x % 1000007
     
# bottom up approach
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B, mydict = {}):
