from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSum = 0
        count = 0
        prefSumMap = defaultdict(int)
        for i in nums:
            prefSum += i
            if prefSum == k:
                count+=1
            if prefSum-k in prefSumMap:
                count += prefSumMap[prefSum-k]
            prefSumMap[prefSum] += 1
        return count
