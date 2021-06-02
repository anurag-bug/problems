https://leetcode.com/problems/single-element-in-a-sorted-array/
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
Follow up: Your solution should run in O(log n) time and O(1) space.
class Solution:
    def singleNonDuplicateHelper(self, nums: List[int], low, high) -> int:
        if low > high:
            return -1
        if low == high:
            return nums[low]
        else:
            mid = (low + high) // 2
            #checking if mid the desired element
            if nums[mid+1] != nums[mid] and nums[mid-1] != nums[mid]:
                return nums[mid]
            else:
                # adjusting mid such that mid is start of the pair
                if nums[mid-1] == nums[mid]:
                    mid = mid-1
                rightCount = high - mid + 1
                # if right half is even means the target element is in left half                 
                if rightCount % 2 == 0:
                    return self.singleNonDuplicateHelper(nums, low, mid-1)
                else:
                    return self.singleNonDuplicateHelper(nums, mid+2, high)
                    
                
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return self.singleNonDuplicateHelper(nums, 0, len(nums)-1)
