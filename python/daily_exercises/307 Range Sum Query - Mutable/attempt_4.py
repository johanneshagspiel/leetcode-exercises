from typing import List
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray:

    def __init__(self, nums: List[int]):

        def create_tree(left, right):

            if left > right:
                return None


            if left == right:
                node = Node(left, right)
                node.total = nums[left]
                return node

            node = Node(left, right)

            mid = left + ((right - left) // 2)

            node.left = create_tree(left, mid)
            node.right = create_tree(mid + 1, right)

            node.total = node.left.total + node.right.total

            return node

        self.root = create_tree(0, len(nums) - 1)


    def update(self, index: int, val: int) -> None:

        def update_tree(root):

            if root.start == root.end:
                root.total = val
                return

            mid = (root.start + root.end) // 2

            if index <= mid:
                update_tree(root.left)
            else:
                update_tree(root.right)

            root.total = root.left.total + root.right.total

            return val

        return update_tree(self.root)


    def sumRange(self, left: int, right: int) -> int:

        def range_sum(node, i, j):

            if node.start == i and node.end == j:
                return node.total

            mid = (node.end + node.start) // 2

            if j <= mid:
                return range_sum(node.left, i, j)

            elif i >= mid + 1:
                return range_sum(node.right, i, j)

            else:
                return range_sum(node.left, i, mid) + range_sum(node.right, mid + 1, j)

        return range_sum(self.root, left, right)




