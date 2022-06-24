from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy_node = ListNode()
        dummy_node.next = head
        prev_node = dummy_node
        current_node = head

        while current_node:
            if current_node.val == val:
                prev_node.next = current_node.next
                current_node = prev_node.next
            else:
                current_node = current_node.next

        return dummy_node.next

