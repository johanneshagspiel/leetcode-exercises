# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        else:

            queue = collections.deque()
            queue.append((root, 1))
            max_width = 0

            while queue:

                queue_len = len(queue)

                start_found = False
                start = 0
                end = 0

                for element in range(queue_len):
                    cur_element, index = queue.popleft()

                    if not start_found:
                        start_found = True
                        start = index
                    end = index

                    if cur_element.left:
                        queue.append((cur_element.left, 2*index))
                    if cur_element.right:
                        queue.append((cur_element.right, 2*index + 1))

                width = end - start + 1
                max_width = max(max_width, width)

            return max_width
