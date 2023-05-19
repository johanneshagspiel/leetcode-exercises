# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        if not head:
            return 0

        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next

        left = 0
        right = len(values) - 1

        maxSum = 0

        while left < right:
            leftVal = values[left]
            rightVal = values[right]
            tempSum = leftVal + rightVal

            maxSum = max(maxSum, tempSum)

            left += 1
            right -= 1

        return maxSum
