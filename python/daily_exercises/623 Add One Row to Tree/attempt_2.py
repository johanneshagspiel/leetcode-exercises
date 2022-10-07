# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return root

        elif depth == 1:
            dummy = TreeNode(val=val)
            dummy.left = root
            return dummy

        queue = collections.deque([root])
        level = 0

        while queue:
            level += 1
            len_queue = len(queue)

            for _ in range(len_queue):

                node = queue.popleft()

                if level == depth - 1:

                    if node.left:
                        prev_left = node.left
                    else:
                        prev_left = None

                    if node.right:
                        prev_right = node.right
                    else:
                        prev_right = None

                    new_left = TreeNode(val=val)
                    new_left.left = prev_left
                    node.left = new_left

                    new_right = TreeNode(val=val)
                    new_right.right = prev_right
                    node.right = new_right

                else:
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

        return root
