Intersecting Chords in a Circle
Problem Description

Given a number A, return number of ways you can draw A chords in a circle with 2 x A points 
such that no 2 chords intersect.

Two ways are different if there exists a chord which is present in one way and not in other.
Return the answer modulo 10^9 + 7.

Catalan numbers
Exp: After drawing a chord b/w 2 points the points get divided b/w two disjoint sets
import sys
sys.setrecursionlimit(999999)
class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A, mydict={}):
        
       # return abs(2*A*(2*A-000))
       if A in mydict:
           return mydict[A]
       if A == 0:
           return 1
       if A == 1:
           return 1
       if A == 2:
           return 2
       else:
           ans = 0
           for k in range(A):
               ans += self.chordCnt(k, mydict) * self.chordCnt(A-k-1,mydict)
           mydict[A] =  ans % (pow(10,9)+7)
       return ans % (pow(10,9)+7)
