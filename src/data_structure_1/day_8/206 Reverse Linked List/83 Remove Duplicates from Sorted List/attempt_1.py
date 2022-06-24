from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur_node = head
        last_seen_value = None
        last_node_with_value = None

        while cur_node:
            cur_value = cur_node.val
            if not last_seen_value:
                last_seen_value = cur_value
                last_node_with_value = cur_node
            else:
                if cur_value != last_seen_value:
                    last_node_with_value.next = cur_node

                    last_seen_value = cur_value
                    last_node_with_value = cur_node


            cur_node = cur_node.next

        last_node_with_value.next = None
        return head
