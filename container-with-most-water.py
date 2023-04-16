You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
https://leetcode.com/problems/container-with-most-water/description/

  
class Solution:
  def maxArea(self, height: List[int]) -> int:
      low = 0
      high = len(height)-1
      ans = 0
      while low < high:
          min_height = min(height[high],height[low])
          ans = max(ans, min_height*(high-low))
          if height[low] < height[high]:
              low +=1
          else:
              high -= 1
      return ans
    
