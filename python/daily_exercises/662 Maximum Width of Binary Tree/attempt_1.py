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
            queue.append(root)

            max_width = 0

            while queue:

                queue_len = len(queue)

                next_start_found = False
                start_found = False

                start = 0
                end = 0

                for element in range(queue_len):
                    cur_element = queue.popleft()

                    if start_found:
                        if cur_element:
                            end = element
                    else:
                        if cur_element:
                            start_found = True
                            start = element

                    if next_start_found:
                        if cur_element:
                            queue.append(cur_element.left)
                            queue.append(cur_element.right)
                        else:
                            queue.append(None)
                            queue.append(None)
                    else:
                        if cur_element:
                            next_start_found = True
                            queue.append(cur_element.left)
                            queue.append(cur_element.right)


                cur_length = end - start + 1
                max_width = max(max_width, cur_length)

                left = 0
                right = len(queue) - 1

                while left < right:
                    if queue[left] == None:
                        left += 1
                    else:
                        break

                while left < right:
                    if queue[right] == None:
                        right -= 1
                    else:
                        break

                queue = queue[left:right+1]

            return max_width
