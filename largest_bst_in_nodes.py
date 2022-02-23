# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
            
    def __init__(self):
        # 0th-> flag if tree is bst
        # 1st-> size of subtree
        # 2nd-> root node of subtree 
        self.ans = (0, 0, None)
        
    def is_bst(self,root, mins, maxs):
        if root == None:
            return (0, 0, None)
        elif root.left == None and root.right==None:
            if root.val>=mins and root.val<maxs :
                self.ans = (1, 1, root)
                return (1, 1, root)
            else:
                return (0, 0, None)
        else:
            leftAns = self.is_bst(root.left, mins, root.val)
            rightAns = self.is_bst(root.right, root.val, maxs)
            # if leftAns[0] and rightAns
            # if root.val >= mins and root
            if leftAns[0] and rightAns[0]:
                if leftAns[2].val <= root.val and rightAns[2].val > root.val:
                    self.ans = (1, leftAns[1]+rightAns[1]+1, root)
                    return self.ans
                else:
                    if leftAns[1] >= rightAns[1]:
                        return (1, leftAns[1], root.left)
                    else:
                        return (1, rightAns[1], root.right)

            else:
                if leftAns[0]:
                    return (1, leftAns[1], root.left)
                elif rightAns[0]:
                    return (1, rightAns[1], root.right)
                else:
                    return (0,0,None)


    def solve(self, root):
        return self.is_bst(root, -9999999999,99999999999)[2]

        
