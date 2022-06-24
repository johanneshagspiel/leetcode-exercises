from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1
        else:
            if list1.val < list2.val:
                remainder = self.mergeTwoLists(list1.next, list2)
                list1.next = remainder
                return list1
            else:
                remainder = self.mergeTwoLists(list1, list2. next)
                list2.next = remainder
                return list2
