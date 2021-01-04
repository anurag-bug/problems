https://leetcode.com/problems/binary-tree-maximum-path-sum/
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.








# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
ans  = -9999999999
class Solution:
    def maxPathSumHelper(self, root: TreeNode) -> int:
        global ans
        if root == None:
            return 0
        else:
            leftPathSum = self.maxPathSumHelper(root.left)
            rightPathSum = self.maxPathSumHelper(root.right)
            # when currNode is in path of max sum
            case1 = max(max(leftPathSum, rightPathSum) + root.val , root.val)
            # when currNode is root of path of max sum
            case2 = max(case1, leftPathSum+rightPathSum+root.val)
            ans = max(case2, ans)
            return case1
    def maxPathSum(self, root: TreeNode, res = 0) -> int:
        global ans
        ans = -999999999999
        self.maxPathSumHelper(root)
        return ans
        
