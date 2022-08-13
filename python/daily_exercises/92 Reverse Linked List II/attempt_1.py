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

        reverse_list = []
        current_position = 0

        dummy = ListNode()
        dummy.next = head

        end = None

        current = dummy

        while current:

            if current_position == (left - 1):
                start = current

            elif current_position >= left and current_position <= right:
                reverse_list.append(current)

            elif current_position == (right + 1):
                end = current

            current = current.next
            current_position += 1

        N = len(reverse_list)

        for position in range(N):
            current = reverse_list[position]
            current.next = end

            end = current

        start.next = end

        return dummy.next
