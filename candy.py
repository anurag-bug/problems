https://leetcode.com/problems/candy/
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candies = [1 for i in range(N)]
        for i in range(1,N):
            if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                candies[i] = candies[i-1]+1
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1]+1
        # print(candies)
        return sum(candies)
