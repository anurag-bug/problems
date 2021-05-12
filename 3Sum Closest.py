https://leetcode.com/problems/3sum-closest/
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closestSum = 999999999999
        numsLength = len(nums)
        for i in range(numsLength-2):
            low = i+1
            high = numsLength-1
            while low < high:
                currSum = nums[i]+nums[low]+nums[high]
                existingDiff = abs(closestSum - target)
                currDiff = abs(currSum - target)
                if currDiff < existingDiff:
                    closestSum = currSum
                if currSum == target:
                    return target
                if currSum < target:
                    low +=1
                else:
                    high -=1
        return closestSum
