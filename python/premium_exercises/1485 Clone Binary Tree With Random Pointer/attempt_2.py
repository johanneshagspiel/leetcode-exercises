# Definition for Node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':

        seen_dic = {}

        def first_iteration(root):

            if not root:
                return root
            else:

                if root in seen_dic:
                    return seen_dic[root]

                else:
                    root_copy = NodeCopy()
                    root_copy.val = root.val

                    seen_dic[root] = root_copy

                    root_copy.left = first_iteration(root.left)
                    root_copy.right = first_iteration(root.right)
                    root_copy.random = first_iteration(root.random)

                    return root_copy

        root_copy = first_iteration(root)

        return root_copy
