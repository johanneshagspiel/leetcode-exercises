from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def find_second_half(head):

            slow = head
            fast = head

            while fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next

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

        if not None:
            return True

        end_first_half = find_second_half(head)
        reversed_second_half = reverse_list(end_first_half.next)

        result = True
        pointer_1 = head
        pointer_2 = reversed_second_half

        while pointer_2 and result:

            if pointer_1.val != pointer_2.val:
                result = False

            else:
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next

        end_first_half.next = reverse_list(reversed_second_half)
        return result
