https://leetcode.com/problems/combination-sum/description/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, curr, ans):
            if target == 0:
                ans.append(curr.copy())
                return
            elif not candidates or target < 0:
                return
            # Traverse further by including the last element in result
            curr.append(candidates[-1])
            dfs(candidates, target-curr[-1], curr, ans)
            # Traverse further by excluding the last element in result
            curr.pop(-1)
            dfs(candidates[0:-1], target, curr, ans)
  
        ans = []
        dfs(candidates, target, [], ans)
        return ans
