# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        listLength = 0
        frontNode = None
        endNode = None

        currentNod = head

        while currentNod:
            listLength += 1

            if endNode:
                endNode = endNode.next

            if listLength == k:
                frontNode = currentNod
                endNode = head

            currentNod = currentNod.next

        temp = frontNode.val
        frontNode.val = endNode.val
        endNode.val = temp

        return head
