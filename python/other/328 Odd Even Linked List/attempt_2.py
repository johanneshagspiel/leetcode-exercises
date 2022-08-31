from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        dummy = ListNode()

        even_head = dummy
        odd_head = head

        start = odd_head

        current = head

        while current and current.next:

            next_even = current.next

            odd_head.next = current.next.next
            even_head.next = next_even

            even_head = even_head.next
            current = odd_head.next

            if current:
                odd_head = odd_head.next

        even_head.next = None
        odd_head.next = dummy.next

        return start
