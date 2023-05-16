# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        valueList = []

        currentNode = head

        while currentNode:
            valueList.append(currentNode.val)
            currentNode = currentNode.next


        firstPosition = k - 1
        firstValue = valueList[firstPosition]

        secondPosition = len(valueList) - k
        secondValue = valueList[secondPosition]

        positionCounter = 0
        currentNode = head

        while currentNode:

            if positionCounter == firstPosition:
                currentNode.val = secondValue

            if positionCounter == secondPosition:
                currentNode.val = firstValue

            currentNode = currentNode.next
            positionCounter += 1

        return head
