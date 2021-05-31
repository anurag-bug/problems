https://leetcode.com/problems/sliding-window-maximum/
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq =deque()
        N = len(nums)
        ans = []
        for i in range(N):
            if i-(k-1) > 0:
                while dq and dq[0] < i-(k-1):
                    dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans[k-1::]
