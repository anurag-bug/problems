https://leetcode.com/problems/largest-rectangle-in-histogram/
Given an array of integers heights representing the histogram's 
bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights)==1:
            return heights[0]
        leftLimit = []
        mystack = []
        N = len(heights)
        for i in range(N):
            # print(mystack)
            if len(mystack)==0:
                leftLimit.append(-1)
                mystack.append(i)
            else:
                while len(mystack) and heights[mystack[-1]] >= heights[i]:
                    mystack.pop()
                if len(mystack) == 0:
                    leftLimit.append(-1)
                else:
                    leftLimit.append(mystack[-1])
                mystack.append(i)
        mystack = []
        rightLimit = []
        for i in range(N-1,-1,-1):
            if len(mystack)==0:
                rightLimit.append(N)
                mystack.append(i)
            else:
                while len(mystack) and heights[mystack[-1]] >= heights[i]:
                    mystack.pop()
                if len(mystack) == 0:
                    rightLimit.append(N)
                else:
                    rightLimit.append(mystack[-1])
                mystack.append(i)
        rightLimit = rightLimit[::-1]
        print(leftLimit)
        print(rightLimit)
        ans = 0
        for i in range(N):
            ans = max(ans, heights[i]*(rightLimit[i]-leftLimit[i]-1))
        return ans
