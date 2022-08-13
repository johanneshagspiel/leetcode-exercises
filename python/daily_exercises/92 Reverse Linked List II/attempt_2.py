from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        distance = right - left

        if distance == 0:
            return head

        dummy = ListNode()
        dummy.next = head

        start = dummy
        end = None
        prev = None

        current = dummy
        current_position = 0

        while current:

            next = current.next

            if current_position == (left - 1):
                start = current

            if current_position == left:
                prev = current

            if current_position >= left and current_position <= right:
                current.next = end
                end = current

            if current_position == (right + 1):
                prev.next = current

            current = next
            current_position += 1

        start.next = end
        return dummy.next
