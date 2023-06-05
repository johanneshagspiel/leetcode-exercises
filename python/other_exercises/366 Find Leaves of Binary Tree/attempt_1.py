# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:


        def test(root, remaining_set):

            stack = []
            stack.append(root)

            level = []

            while stack:

                node = stack.pop()

                if node in remaining_set:
                    if (node.left and node.left not in remaining_set) or (node.right and node.right not in remaining_set):
                        if node.left:
                            stack.append(node.left)
                        if node.right:
                            stack.append(node.right)

                    else:
                        level.append(node.val)
                        remaining_set.pop(node)

            return level, remaining_set



        if not root:
            return root

        res = []
        remaining_set = set()

        stack = []
        stack.append(root)

        level = []

        while stack:

            node = stack.pop()

            if node.left or node.right:
                remaining_set.add(node)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            else:
                level.append(node.val)

        res.append(level)

        keep_going = True

        while keep_going:

            level, remaining_set = test(root, remaining_set)
            res.append(level)

            if len(remaining_set) == 0:
                keep_going = False

        return res
