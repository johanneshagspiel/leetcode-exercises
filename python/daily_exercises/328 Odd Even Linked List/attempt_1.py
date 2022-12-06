# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        even_list = [float("inf")] * (pow(10, 4))
        odd_list = [float("inf")] * (pow(10, 4))

        start = head
        root = head

        count = 1
        even_ind = 0
        odd_ind = 0

        while head:
            if count % 2 == 1:
                odd_list[odd_ind] = head.val
                odd_ind += 1
            else:
                even_list[even_ind] = head.val
                even_ind += 1
            count += 1
            head = head.next

        even_ind = 0
        odd_ind = 0
        odd_mode = True

        while start:
            if odd_list[odd_ind] == float("inf"):
                odd_mode = False

            if odd_mode:
                start.val = odd_list[odd_ind]
                odd_ind += 1
            else:
                start.val = even_list[even_ind]
                even_ind += 1
            start = start.next

        return root
