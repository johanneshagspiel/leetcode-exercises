from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(val=-1)
        previous = dummy

        while head:
            if head.val == previous.val:
                previous.next = head.next
            else:
                previous = head

            head = head.next

        return dummy.next