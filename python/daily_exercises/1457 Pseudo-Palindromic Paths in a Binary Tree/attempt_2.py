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

        palindromic_count = 0

        def can_be_palindormic(counter_dic):
            nonlocal palindromic_count

            odd_encountered = False
            palindromic = True

            for count in counter_dic.values():
                if count % 2 == 1:
                    if odd_encountered:
                        palindromic = False
                        break
                    else:
                        odd_encountered = True

            if palindromic:
                palindromic_count += 1


        stack = []
        stack.append((root, {}))

        while stack:

            node, counter = stack.pop()

            if node.val not in counter:
                counter[node.val] = 0
            counter[node.val] += 1

            if not node.left and not node.right:
                can_be_palindormic(counter)
            else:
                if node.left:
                    new_counter = copy.deepcopy(counter)
                    stack.append((node.left, new_counter))
                if node.right:
                    new_counter = copy.deepcopy(counter)
                    stack.append((node.right, new_counter))

        return palindromic_count
