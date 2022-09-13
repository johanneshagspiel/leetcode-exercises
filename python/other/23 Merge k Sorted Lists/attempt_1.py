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

        move_dic = {}
        status_dic = {}

        for index in range(n):
            move_dic[index] = 0
            status_dic[index] = False

        finished = 0

        while keep_going:

            min_node_val = float("inf")
            min_node_index = -1

            for index in range(n):

                if status_dic[index] == False:

                    node_position = move_dic[index]
                    node = lists[index]

                    for position in range(node_position):
                        node = node.next

                    if node:
                        if node.val < min_node_val:
                            min_node_val = node.val
                            min_node_index = index
                    else:
                        if status_dic[index] == False:
                            status_dic[index] = True
                            finished += 1

            if min_node_index != -1:
                new_node = ListNode(val=min_node_val)
                prev.next = new_node
                prev = prev.next

                move_dic[min_node_index] += 1

            elif finished == n or min_node_index == -1:
                keep_going = False

        return dummy.next
