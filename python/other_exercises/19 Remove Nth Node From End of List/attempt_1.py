from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return head

        start = head

        total_count = 0
        while head:
            head = head.next
            total_count += 1

        amount_to_move = total_count - n


        dummy = ListNode()
        dummy.next = start
        prev_node = dummy

        while amount_to_move:
            prev_node = prev_node.next
            amount_to_move -= 1

        next_node = prev_node.next.next

        prev_node.next = next_node
        next_node.prev = prev_node

        return dummy.next
