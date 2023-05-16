# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        dummy = ListNode()
        dummy.next = head

        length = 0
        currentNode = head

        while currentNode:
            length += 1
            currentNode = currentNode.next

        firstPosition = k - 1
        secondPosition = length - k

        if firstPosition > secondPosition:
            temp = secondPosition
            secondPosition = firstPosition
            firstPosition = temp

        firstNode = None
        firstValue = -1

        secondValue = -1

        positionCounter = 0
        currentNode = head
        while currentNode:

            if positionCounter == firstPosition:
                firstNode = currentNode
                firstValue = currentNode.val

            if positionCounter == secondPosition:
                secondValue = currentNode.val
                currentNode.val = firstValue

            currentNode = currentNode.next
            positionCounter += 1

        firstNode.val = secondValue

        return dummy.next

