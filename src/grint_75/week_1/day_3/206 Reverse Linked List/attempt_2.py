from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:
            prev_node = None

            while head.next:

                next_node = head.next
                head.next = prev_node

                prev_node = head
                head = next_node

            head.next = prev_node

        return head