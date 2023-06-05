from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev_node = n_node = next_node = fast = head

        move_counter = 0
        for node in range(n - 1):
            fast = fast.next
            if move_counter == 0:
                next_node = next_node.next
            move_counter += 1

        counter = 0

        while fast.next:
            fast = fast.next

            if counter == 0:
                next_node = next_node.next
            elif counter == 1:
                next_node = next_node.next
                n_node = n_node.next
            else:
                next_node = next_node.next
                n_node = n_node.next
                prev_node = prev_node.next

            counter += 1


        prev_node.next = next_node
        n_node.next = None

        return  head
