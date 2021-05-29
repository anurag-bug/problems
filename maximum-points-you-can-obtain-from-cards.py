https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

With Help # sliding window
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        currSum = 0
        ans = 0
        for i in range(k):
            currSum += cardPoints[i]
        low = k-1
        high = len(cardPoints)-1
        ans = max(ans, currSum)
        while low >= 0 and high >=0:
            currSum -= cardPoints[low]
            currSum += cardPoints[high]
            low -= 1
            high -= 1
            ans = max(ans, currSum)
        return ans
