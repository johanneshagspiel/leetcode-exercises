from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        dummy = ListNode()

        current_even_node = dummy
        current_odd_node = head


        while True:

            next_even_node = current_odd_node.next

            current_odd_node.next = current_odd_node.next.next

            current_even_node.next = next_even_node
            current_even_node = current_even_node.next

            if current_odd_node.next:
                current_odd_node = current_odd_node.next
            else:
                break


        current_even_node.next = None
        current_odd_node.next = dummy.next

        return head
