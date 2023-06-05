from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        elif len(lists) == 1:
            return lists[0]

        amount = len(lists)
        interval = 1

        while interval < amount:

            for index in range(0, amount - interval, interval * 2):
                lists[index] = self.mergeTwoLists(lists[index], lists[index + interval])
            interval *= 2

        return lists[0]


    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        prev = dummy

        keep_going = True

        while keep_going:

            if list1 and list2:

                if list1.val < list2.val:
                    prev.next = list1
                    prev = prev.next
                    list1 = list1.next
                else:
                    prev.next = list2
                    prev = prev.next
                    list2 = list2.next

            else:
                if list1:
                    prev.next = list1
                elif list2:
                    prev.next = list2

                keep_going = False

        return dummy.next
