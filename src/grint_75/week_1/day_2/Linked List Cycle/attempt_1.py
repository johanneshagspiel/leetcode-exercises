from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_dic = {}
        return self.hasCycle_Helper(head, seen_dic)

    def hasCycle_Helper(self, head, dic) -> bool:
        if not head or not head.next:
            return False
        else:
            if head in dic:
                return True
            else:
                dic[head] = True
                return self.hasCycle_Helper(head.next, dic)