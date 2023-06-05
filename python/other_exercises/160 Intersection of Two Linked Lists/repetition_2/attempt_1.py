from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        startA = headA
        startB = headB

        while headA != headB:

            if not headA:
                headA = startB
            else:
                headA = headA.next

            if not headB:
                headB = startA
            else:
                headB = headB.next

        return headA
