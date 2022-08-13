from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_node = ListNode()
        prev_node = dummy_node

        while list1 or list2:
            if list1.val < list2.val:
                prev_node.next = list1
                prev_node = list1
            else:
                prev_node.next = list2
                prev_node = list2

        if list1:
            prev_node.next = list1

        if list2:
            prev_node.next = list2

        return dummy_node.next