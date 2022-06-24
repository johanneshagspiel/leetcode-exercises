from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if (head is None) or (head.next is None):
            return head

        p = self.reverseList(head.next)
        head.next.next = self
        head.next = None
        return p