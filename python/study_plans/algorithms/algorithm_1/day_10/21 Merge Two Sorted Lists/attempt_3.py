from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode()

        prev = dummy
        keep_going = True

        while keep_going:

            if list1 and list2:

                if list1.val < list2.val:
                    prev.next = list1
                    list1 = list1.next
                    prev = prev.next

                else:
                    prev.next = list2
                    list2 = list2.next
                    prev = prev.next

            elif list1:
                prev.next = list1
                keep_going = False

            elif list2:
                prev.next = list2
                keep_going = False

            else:
                keep_going = False

        return dummy.next
