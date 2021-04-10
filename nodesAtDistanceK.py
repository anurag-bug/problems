All Nodes Distance K in Binary Tree
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

class Solution:
    def traverse(self, root, pMap, parent):
        if root == None:
            return
        else:
            
            self.traverse(root.left,pMap, root)
            self.traverse(root.right,pMap,root)
            pMap[root] = parent
            
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parentMap = {}
        self.traverse(root,parentMap, None)
        queue = [target]
        currLevel = 0
        visited = set()
        while queue and currLevel < K:
            # for i in queue:
            #     print(i.val)
            # print()
            N = len(queue)
            currLevel+=1
            for _ in range(N):
                front = queue.pop(0)
                visited.add(front)
                if front.left and front.left not in visited:
                    queue.append(front.left)
                if front.right and front.right not in visited:
                    queue.append(front.right)
                if parentMap[front] and parentMap[front] not in visited:
                    queue.append(parentMap[front])
        ans = []
        for i in queue:
            ans.append(i.val)
        return ans
