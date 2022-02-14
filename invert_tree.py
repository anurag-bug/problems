# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root == None:
            return root
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.solve(root.left)
            self.solve(root.right)
            return root
