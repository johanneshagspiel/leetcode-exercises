from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def get_midway_node(head):

            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def reverse_list(head):

            prev = None
            cur = head

            while cur:
                next = cur.next

                cur.next = prev

                prev = cur
                cur = next

            return prev


        if not head:
            return True

        end_first_half = get_midway_node(head)
        start_second_half = reverse_list(end_first_half.next)

        first_pointer = head
        second_pointer = start_second_half

        equal = True

        while second_pointer and equal:
            if first_pointer.val != second_pointer.val:
                equal = False
            else:
                first_pointer = first_pointer.next
                second_pointer = second_pointer.next

        end_first_half.next = reverse_list(start_second_half)

        return equal
