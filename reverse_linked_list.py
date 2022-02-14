# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
Given a singly linked list node, return its reverse.

Bonus: Can you do this in \mathcal{O}(1)O(1) space?
  
class Solution:
    def solve(self, node, prev=None):
        if node is None:
            return node
        if node.next == None:
            node.next = prev
            return node
        next_node = node.next
        node.next = prev
        return self.solve(next_node, node)
        
