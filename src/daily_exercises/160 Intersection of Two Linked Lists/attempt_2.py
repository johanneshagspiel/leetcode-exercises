from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None

        else:

            pointerA = headA
            pointerB = headB

            while pointerA != pointerB:
                pointerA = headB if pointerA == None else pointerA.next
                pointerB = headA if pointerB == None else pointerB.next

            return pointerA