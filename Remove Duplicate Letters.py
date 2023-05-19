Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order among all possible results.
https://leetcode.com/problems/remove-duplicate-letters/description/
Input: s = "bcabc"
Output: "abc"
Input: s = "cbacdcbc"
Output: "acdb"
  
from collections import defaultdict, Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited=defaultdict(bool)
        counter = Counter(s)
        mystack = []
        for i in s:
            if not mystack:
                mystack.append(i)
                visited[i] = True
                counter[i] -= 1
                # print('here')
                continue
            else:
                if visited[i]:
                    counter[i] -= 1
                    continue
                while mystack and mystack[-1] > i:
                    if counter[mystack[-1]] > 0:
                        visited[mystack[-1]] = False
                        mystack.pop(-1)
                    else:
                        break
            mystack.append(i)
            visited[i] = True
            counter[i] -= 1
        return "".join(mystack)
