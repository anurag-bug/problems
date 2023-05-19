Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
https://leetcode.com/problems/longest-palindrome/description/

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        flag = False
        for key in counter:
            if counter[key] == 1:
                flag = True
                res += 1
                break
        count_tuple = counter.items()
        counter_tuple = sorted(count_tuple, key=lambda x: -x[1])
        # print(counter_tuple)
        for key, val in counter_tuple:
            print(key,val)
            if val%2 != 0:
                if not flag:
                    res += val
                    flag = True
                else:
                    res += (val-1)
            else:
                res += val
        return res
