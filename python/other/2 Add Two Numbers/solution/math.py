from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0

        dummy_node = ListNode()
        previous = dummy_node

        while l1 or l2 or carry:
            combined = carry
            if l1:
                combined += l1.val
                l1 = l1.next
            if l2:
                combined += l2.val
                l2 = l2.next

            carry = combined // 10
            result = combined % 10

            new_node = ListNode(result)
            previous.next = new_node
            previous = new_node

        return dummy_node.next
