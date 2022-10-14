# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        count = head
        n = -1

        while count.next:
            n += 1
            count = count.next

        target = (n // 2)

        move = head

        if target == -1:
            dummy.next = None
            return dummy.next

        else:
            while target > 0:
                move = move.next
                target -= 1

            move.next = move.next.next

            return dummy.next
