from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        dummy = ListNode(-math.inf)
        dummy.next = head
        current = dummy
        changed = False

        prev_smaller = dummy
        prev = dummy
        first_x_position = current

        x_found = False

        while current:
            next = current.next

            if not x_found:

                if current.val >= x:
                    x_found = True
                    first_x_position = current
                else:
                    prev_smaller = current

            else:

                if current.val < x:
                    prev.next = next
                    current.next = first_x_position
                    prev_smaller.next = current

                    prev_smaller = current
                    changed = True

            if changed:
                changed = False
            else:
                prev = current
            current = next


        return dummy.next
