# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        right_start = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(right_start)

        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode()
        prev = dummy

        while left and right:
            if left.val < right.val:
                prev.next = left
                left = left.next
            else:
                prev.next = right
                right = right.next
            prev = prev.next

        if left:
            prev.next = left

        if right:
            prev.next = right

        return dummy.next

