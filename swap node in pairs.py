https://leetcode.com/problems/swap-nodes-in-pairs/
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        curr = head
        nxt = curr.next
        nxt_to_nxt = nxt.next
        nxt.next = curr
        curr.next = self.swapPairs(nxt_to_nxt)
        return nxt
