from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        else:
            dummy_head = ListNode()
            dummy_head.next = head

            previous_node = dummy_head
            current_node = head
            next_node = current_node.next
            duplicate_encountered = False

            while next_node:
                if duplicate_encountered:
                    if next_node.val != current_node.val:
                        previous_node.next = next_node
                        current_node = next_node
                        duplicate_encountered = False
                    else:
                        None
                else:
                    if next_node.val != current_node.val:
                        previous_node = current_node
                        current_node = next_node
                    else:
                        duplicate_encountered = True
                        previous_node.next = None

                next_node = next_node.next

            return dummy_head.next

if __name__ == "__main__":
    solution = Solution()
    solution.deleteDuplicates()