from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        val_list = []

        while head:
            val_list.append(head.val)
            head = head.next

        left = 0
        right = len(val_list) - 1

        while left < right:
            num_l = val_list[left]
            nuum_r = val_list[right]

            if num_l != nuum_r:
                return False
            else:
                left += 1
                right -= 1

        return True
    
