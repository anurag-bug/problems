https://leetcode.com/problems/subarrays-with-k-different-integers/
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

class Solution:
    def countSubArrays(self, A, K):
        ans = 0
        mydict = {}
        N = len(A)
        distinct = 0
        j = 0
        for i in range(N):
            if A[i] not in mydict:
                mydict[A[i]] = 1
                distinct += 1
            else:
                mydict[A[i]] += 1
            if distinct <= K:
                ans += (i-j+1)
            else:
                while j <=i and distinct > K:
                    mydict[A[j]]-=1
                    if mydict[A[j]] == 0:
                        del mydict[A[j]]
                        distinct-=1
                    j+=1
                ans+= (i-j+1)
        return ans
            
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.countSubArrays(A,K)-self.countSubArrays(A,K-1)
