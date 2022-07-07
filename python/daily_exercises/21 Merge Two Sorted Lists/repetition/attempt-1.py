from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_node = ListNode()
        previous = dummy_node

        while list1 and list2:

            if not list1:
                previous.next = list2

            elif not list2:
                previous.next = list1

            else:
                if list1.val <= list2.val:
                    previous.next = list1
                    list1 = list1.next
                else:
                    previous.next = list2
                    list2 = list2.next

                previous = previous.next

        return dummy_node.next
