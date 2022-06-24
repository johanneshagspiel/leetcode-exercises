from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_start = ListNode(-1)
        self.recursive_merge_lists(dummy_start, list1, list2)
        return dummy_start.next

    def recursive_merge_lists(self, prev_node, list1, list2):

        if not list1 and not list2:
            return
        elif not list1 and list2:
            prev_node.next = list2
            return
        elif list1 and not list2:
            prev_node.next = list1
            return
        else:
            if list1.val <= list2.val:
                prev_node.next = list1
                self.recursive_merge_lists(prev_node.next, list1.next, list2)
            else:
                prev_node.next = list2
                self.recursive_merge_lists(prev_node.next, list1, list2.next)
