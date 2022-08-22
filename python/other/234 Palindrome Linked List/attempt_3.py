from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse_list(root):

            prev = None
            current = root

            while current:
                next = current.next

                current.next = prev

                prev = current
                current = next

            return prev

        slow_pointer = head
        fast_mover = head

        while fast_mover.next and fast_mover.next.next:
            slow_pointer = slow_pointer.next
            fast_mover = fast_mover.next.next

        start_point_2 = reverse_list(slow_pointer.next)
        start_point_1 = head

        equal = True

        while start_point_2 and equal:
            if start_point_1.val != start_point_2.val:
                equal = False
            else:
                start_point_1 = start_point_1.next
                start_point_2 = start_point_2.next

        return equal