from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None

        else:
            node_a_dic = {}
            current_node_a = headA
            while current_node_a:

                node_a_dic[current_node_a] = True
                current_node_a = current_node_a.next


            current_node_b = headB
            while current_node_b:
                if current_node_b in node_a_dic:
                    return current_node_b

            return None