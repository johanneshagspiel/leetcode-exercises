# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        head = list1

        for move in range(a-1):
            list1 = list1.next

        a_pointer = list1

        for move in range(b-a+2):
            list1 = list1.next

        b_pointer = list1

        a_pointer.next = list2

        while list2.next:
            list2 = list2.next

        list2.next = b_pointer

        return head