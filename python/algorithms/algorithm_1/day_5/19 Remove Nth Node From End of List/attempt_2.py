from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head

        first_pointer = second_pointer = dummy_node

        for move in range(n + 1):
            first_pointer = first_pointer.next

        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        two_ahead = second_pointer.next.next
        second_pointer.next = two_ahead

        return dummy_node.next