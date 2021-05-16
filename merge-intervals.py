https://leetcode.com/problems/merge-intervals/

  class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        finalAns = []
        prevInterval = None
        for interval in intervals:
            if prevInterval == None:
                finalAns.append(interval)
                prevInterval = interval
            else:
                if prevInterval[1] >= interval[0]:
                    finalAns.pop()
                    # prevInterval
                    finalAns.append((prevInterval[0], max(interval[1], prevInterval[1])))
                    prevInterval = (prevInterval[0], max(interval[1], prevInterval[1]))
                else:
                    finalAns.append(interval)
                    prevInterval = interval
        return finalAns
