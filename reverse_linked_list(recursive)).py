https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode, prev=None) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            head.next = prev
            return head
        nxt = head.next
        head.next = prev
        return self.reverseList(nxt, head)
        
        
