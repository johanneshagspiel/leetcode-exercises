
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        left_node_list = []
        right_node_list = []

        def find(node, val, left):
            if node:
                if left:
                    left_node_list.append(node)
                else:
                    right_node_list.append(node)

                if node.val == val:
                    return
                else:
                    if node.val > val:
                        find(node.left, val, left)
                    else:
                        find(node.right, val, left)

        find(root, p.val, True)
        find(root, q.val, False)

        list_1 = left_node_list[::]
        list_1.extend(right_node_list)

        list_2 = right_node_list[::]
        list_2.extend(left_node_list)

        pointer_1 = 0
        pointer_2 = 0

        while list_1[pointer_1] != list_2[pointer_2]:
            pointer_1 += 1
            pointer_2 += 1

        return list_1[pointer_1]
