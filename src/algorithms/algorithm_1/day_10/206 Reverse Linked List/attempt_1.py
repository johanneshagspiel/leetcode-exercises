from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        else:
            previous_node = head

            if previous_node.next:
                current_node = previous_node.next
                previous_node.next = None

                while current_node:
                    next_node = current_node.next

                    current_node.next = previous_node
                    previous_node = current_node
                    current_node = next_node

                return previous_node

            else:
                return previous_node
