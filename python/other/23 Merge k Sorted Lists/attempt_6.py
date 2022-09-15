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

        interval = 1
        amount = len(lists)

        while interval < amount:
            for index in range(0, amount - interval, interval * 2):
                lists[index] = self.mergeTwoLists(lists[index], lists[index + interval])
            interval *= 2

        return lists[0]

    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        prev = dummy

        while list1 and list2:

            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
                prev = prev.next
            else:
                prev.next = list2
                list2 = list2.next
                prev = prev.next

        if list1:
            prev.next = list1

        if list2:
            prev.next = list2

        return dummy.next

