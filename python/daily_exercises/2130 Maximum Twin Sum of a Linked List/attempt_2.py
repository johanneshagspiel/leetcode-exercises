# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        def reverseList(head):

            prev = ListNode()
            prev.next = head

            current = head
            next = head.next

            while current:
                current.next = prev

                prev = current
                current = next

                next = next.next

            return prev


        if not head:
            return 0


        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverseList(slow)

        return slow
