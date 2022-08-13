class Node:
    def __init__(self, start, end):
        self.total = 0
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class NumArray(object):
    def __init__(self, nums):

        def build_tree(nums, l, r):

            if l > r:
                return None

            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n

            mid = l + ((r - l) // 2)

            root = Node(l, r)
            root.left = build_tree(nums, l, mid)
            root.right = build_tree(nums, mid+1, r)

            root.total = root.left.total + root.right.total

            return root

        self.root = build_tree(nums, 0, len(nums)-1)

    def update(self, i, val):

        def update_val(root, i, val):

            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end) // 2

            if i <= mid:
                update_val(root.left, i, val)

            else:
                update_val(root.right, i, val)

            root.total = root.left.total + root.right.total

            return root.total

        return update_val(self.root, i, val)

    def sumRange(self, i, j):

        def range_sum(root, i, j):

            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) // 2

            if j <= mid:
                return range_sum(root.left, i, j)

            elif i >= mid + 1:
                return range_sum(root.right, i, j)

            else:
                return range_sum(root.left, i, mid) + range_sum(root.right, mid+1, j)

        return range_sum(self.root, i, j)


