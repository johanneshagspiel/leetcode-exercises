from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        start_a = headA
        start_b = headB

        while headA != headB:

            if headA == None:
                headA = start_b
            else:
                headA = headA.next

            if headB == None:
                headB = start_a
            else:
                headB = headB.next

        return headA