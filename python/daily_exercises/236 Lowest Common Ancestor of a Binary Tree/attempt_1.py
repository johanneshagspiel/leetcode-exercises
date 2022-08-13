# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        node = root

        while node:

            if node.left and node.right:
                remaining_node = None
                smaller_node = node.left if node.left.val < node.right.val else node.right
                larger_node = node.left if node.left.val > node.right.val else node.right
            elif node.left or node.right:
                remaining_node = node.left if node.left else node.right
                smaller_node = None
                larger_node = None
            else:
                return node

            if node.val >= p.val and node.val >= q.val:

                if smaller_node:
                    if smaller_node.val <= p.val and smaller_node.val <= q.val:
                        node = smaller_node
                    else:
                        return node

                elif remaining_node:
                    if remaining_node.val <= p.val and remaining_node.val <= q.val:
                        node = remaining_node
                    else:
                        return node
                else:
                    return node

            elif node.val <= p.val and node.val <= q.val:
                if larger_node:
                    if larger_node.val >= p.val and larger_node.val >= q.val:
                        node = larger_node
                    else:
                        return node

                elif remaining_node:
                    if remaining_node.val >= p.val and remaining_node.val >= q.val:
                        node = remaining_node
                    else:
                        return node
                else:
                    return node

            else:
                return node
