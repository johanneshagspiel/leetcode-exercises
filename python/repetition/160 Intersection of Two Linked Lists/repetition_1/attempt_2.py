from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        start_b = headB

        while headA:
            while headB:
                if headA == headB:
                    return headA
                else:
                    headB = headB.next
            headA = headA.next
            headB = start_b

        return None
