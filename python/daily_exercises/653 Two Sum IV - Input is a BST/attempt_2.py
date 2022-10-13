# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        if not root:
            return False

        number_dic = collections.defaultdict(int)

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            number_dic[node.val] += 1

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        for number, occurences in number_dic.items():
            complement = k - number

            if complement in number_dic:
                if complement == number:
                    if occurences > 1:
                        return True
                else:
                    return True

        return False