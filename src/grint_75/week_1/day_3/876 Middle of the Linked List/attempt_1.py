from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_seen = []

        while head:
            nodes_seen.append(head)
            head = head.next

        amount_nodes_seen = len(nodes_seen)

        return nodes_seen[(amount_nodes_seen // 2)]