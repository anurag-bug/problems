https://leetcode.com/problems/first-missing-positive/
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #use index as hash for counter
        counter = [0 for i in range(len(nums)+1)]
        counter[0] = 1
        N = len(nums)
        for i in nums:
            if i < 1 or i > N:
                continue
            else:
                counter[i]+=1
        for index, i in enumerate(counter):
            if i == 0:
                return index
        return N+1
        
