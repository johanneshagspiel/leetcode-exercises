from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_node = ListNode()

        def rec(list1, list2, previous_node):
            if not list1:
                previous_node.next = list2

            elif not list2:
                previous_node.next = list1

            else:

                if list1.val <= list2.val:
                    previous_node.next = list1
                    rec(list1.next, list2, previous_node.next)

                else:
                    previous_node.next = list2
                    rec(list1, list2.next, previous_node.next)

        rec(list1, list2, dummy_node)
        return dummy_node.next
