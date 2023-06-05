from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 and list2:
            if list1.val > list2.val:
                return self.mergeTwoLists_with_start(list1, list1.next, list2)
            else:
                return self.mergeTwoLists_with_start(list2, list2.next, list1)
        elif list1:
            return list1
        elif list2:
            return list2
        else:
            return None

    def mergeTwoLists_with_start(self, start_node, list1: Optional[ListNode], list2: Optional[ListNode]):

        if list1 and list2:
            if list1.val > list2.val:
                start_node.next = list1
                self.mergeTwoLists_with_start(start_node, list1.next, list2)
            else:
                start_node.next = list2
                self.mergeTwoLists_with_start(start_node, list2.next, list1)

        elif list1:
            start_node.next = list1
        elif list2:
            start_node.next = list2
        else:
            start_node


if __name__ == '__main__':
    solution = Solution()

    list1 = [1,2,4]
    list2 = [1,3,4]
    output_1 = solution.mergeTwoLists(list1, list2)
    expected_output = [1,1,2,3,4,4]
    print(output_1)
