import collections
import copy
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        palindromic_num = 0

        def can_be_palindromic(path_list):
            nonlocal palindromic_num

            value_counter = collections.Counter(path_list)

            odd_encountered = False
            palindromic = True

            for num, value in value_counter.items():
                if value % 2 == 1:
                    if odd_encountered:
                        palindromic = False
                    else:
                        odd_encountered = True

            if palindromic:
                palindromic_num += 1


        stack = []
        stack.append((root, []))

        while stack:
            node, prev_path = stack.pop()
            prev_path.append(node.val)

            if not node.left and not node.right:
                can_be_palindromic(prev_path)

            else:
                if node.left:
                    new_path = copy.deepcopy(prev_path)
                    stack.append((node.left, new_path))
                if node.right:
                    new_path = copy.deepcopy(prev_path)
                    stack.append((node.right, new_path))

        return palindromic_num
