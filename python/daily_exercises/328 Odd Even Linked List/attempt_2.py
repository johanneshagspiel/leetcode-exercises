# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        odd_head = ListNode()
        odd_head.next = head

        even_head = ListNode()

        prev_odd = head
        prev_even = even_head

        odd_mode = False

        head = head.next

        while head:
            if not odd_mode:
                prev_even.next = head
                prev_even = prev_even.next

            else:
                prev_odd.next = head
                prev_odd = prev_odd.next

            head = head.next
            if odd_mode:
                odd_mode = False
            else:
                odd_mode = True

        prev_even.next = None
        prev_odd.next = even_head.next

        return odd_head.next
