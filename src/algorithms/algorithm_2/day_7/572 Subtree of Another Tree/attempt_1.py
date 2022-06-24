import collections
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def check_subtree(root, sub_root):

            queue = collections.deque()
            queue.append((root, sub_root))

            while queue:
                node_1, node_2 = queue.popleft()

                if node_1 and node_2:
                    if node_1.val != node_2.val:
                        return False
                elif node_1 and not node_2:
                    return False
                elif not node_1 and node_2:
                    return False

                if node_1.left and node_2.left:
                    queue.append((node_1.left, node_2.left))
                elif (node_1.left and not node_2.left) or (not node_1.left and node_2.left):
                    return False

                if node_1.right and node_2.right:
                    queue.append((node_1.right, node_2.right))
                elif (node_1.right and not node_2.right) or (not node_1.right and node_2.right):
                    return False

            return True


        queue = collections.deque()
        queue.append(root)

        while queue:
            current_node = queue.popleft()

            if current_node.val == subRoot.val:
                subtree = check_subtree(current_node, subRoot)
                if subtree:
                    return True
                else:
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
            else:
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return False
