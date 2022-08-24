from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        def get_halfway_point(root):

            slow = root
            fast = root

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow


        def reverse_list(root):

            prev = None
            current = root

            while current:
                next = current.next

                current.next = prev

                prev = current
                current = next

            return prev


        end_first_half = get_halfway_point(head)
        start_second_half = reverse_list(end_first_half.next)

        equal = True

        first_pointer = head
        second_pointer = start_second_half

        while second_pointer and equal:
            if first_pointer.val != second_pointer.val:
                equal = False
            else:
                first_pointer = first_pointer.next
                second_pointer = second_pointer.next

        end_first_half.next = reverse_list(start_second_half)
        return equal
