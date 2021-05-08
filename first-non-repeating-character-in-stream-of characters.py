#https://www.interviewbit.com/problems/first-non-repeating-character-in-a-stream-of-characters/
#First non-repeating character in a stream of characters
#Given a string A denoting a stream of lowercase alphabets. You have to make new string B.
#B is formed such that we have to find first non-repeating character each time a 
#character is inserted to the stream and append it at the end to B. If no non-repeating character is found then append '#' at the end of B.
from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        myMap = {}
        ans = []
        dq = deque()
        for i in A:
            if i not in myMap:
                dq.append(i)
            else:
                try:
                    dq.remove(i)
                except: 
                    pass
            myMap[i] = True
            if dq:
                ans.append(dq[0])
            else:
                ans.append("#")
        return "".join(ans)
