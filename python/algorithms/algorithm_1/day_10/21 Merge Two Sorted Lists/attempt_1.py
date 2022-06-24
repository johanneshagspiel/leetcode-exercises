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
            elif not list2:
                return list1
            elif not list1 or not list2:
                return None
            else:
                head_1 = list1
                head_2 = list2

                if head_1.val < head_2.val:
                    previous = head_1
                    head_1 = head_1.next
                else:
                    previous = head_2
                    head_2 = head_2.next

                root = previous

                while head_1 and head_2:
                    if head_1.val < head_2.val:
                        previous.next = head_1
                        head_1 = head_1.next
                    else:
                        previous.next = head_2
                        head_2 = head_2.next

                    previous = previous.next

                if head_1:
                    previous.next = head_1
                if head_2:
                    previous.next = head_2

                return root

