from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode()
        prev = dummy

        keep_going = True
        n = len(lists)

        while keep_going:

            min_node_val = float("inf")
            min_node_index = -1

            for index in range(n):

                node = lists[index]

                if node:
                    if node.val < min_node_val:
                        min_node_val = node.val
                        min_node_index = index

            if min_node_index != -1:
                new_node = ListNode(val=min_node_val)
                prev.next = new_node
                prev = prev.next

                node = lists[min_node_index]
                lists[min_node_index] = node.next

            else:
                keep_going = False

        return dummy.next
