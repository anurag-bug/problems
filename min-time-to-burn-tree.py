Burn a Tree
Given a binary tree denoted by root node A and a leaf node B from this tree.

It is known that all nodes connected to a given node (left child, right child and parent) get burned in 1 second. Then all the nodes which are connected through one intermediate get burned in 2 seconds, and so on.

You need to find the minimum time required to burn the complete binary tree.

import sys
sys.setrecursionlimit(99999999)
from collections import deque
def getParent(A, root, myDict):
    if A == None:
        return
    else:
        myDict[A] = root
        getParent(A.left, A, myDict)
        getParent(A.right, A, myDict)
def findNode(A, B, ans):
    if A == None:
        return 
    else:
        if A.val == B:
            ans.append(A)
            return
        else:
            findNode(A.left, B, ans)
            findNode(A.right, B, ans)
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        parentMap = {}
        getParent(A, None, parentMap)
        ans = -1
        queue = deque()
        x = []
        findNode(A, B, x)
        queue.append(x[0])
        visited = set()
        while queue:
            temp = deque()
            if queue:
                ans+=1
            while queue:
                front = queue.popleft()
                visited.add(front.val) 
                if front.left and front.left.val not in visited:
                    temp.append(front.left)
                if front.right and front.right.val not in visited:
                    temp.append(front.right)
                if parentMap[front] and parentMap[front].val not in visited:
                    temp.append(parentMap[front])
            queue = temp
        return ans 
