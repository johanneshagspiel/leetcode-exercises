import copy
import heapq
from typing import List

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 0
        self.left = None
        self.right = None


class Segment_Tree:

    def __init__(self, nums):

        def build_tree(nums, left, right):
            node = Node(nums[left], nums[right])

            if left == right:
                return node

            if left > right:
                return None

            mid = left + ((right - left) // 2)
            node.left = build_tree(nums, left, mid)
            node.right = build_tree(nums, mid+1, right)

            return node

        self.root = build_tree(nums, 0, len(nums) - 1)

    def query(self, left, right):

        def query_tree(node, left, right):

            if not node:
                return 0

            if node.start >= left and node.end <= right:
                return node.count

            if node.start > right or node.end < left:
                return 0

            return query_tree(node.left, left, right) + query_tree(node.right, left, right)

        return query_tree(self.root, left, right)

    def update(self, val):

        def update_tree(node, val):

            if node.start <= val <= node.end:

                node.count += 1

                if node.left:
                    update_tree(node.left, val)

                if node.right:
                    update_tree(node.right, val)

        update_tree(self.root, val)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        input = sorted(list(set(nums)))
        tree = Segment_Tree(nums=input)

        res = []

        for num in reversed(nums):
            res.append(tree.query(-float("inf"), num-1))
            tree.update(num)

        return res[::-1]
