from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.input_array = nums
        self.input_array.sort()
        self.N = len(self.input_array)

        self.segment_tree = [0] * (4 * self.N)
        self._build_tree(0, 0, self.N - 1)

    def _build_tree(self, tree_index, left, right):

        if left == right:
            self.segment_tree[tree_index] = self.input_array[right]
            return

        mid = left + ((right - left) // 2)
        self._build_tree(2 * tree_index + 1, left, mid)
        self._build_tree(2 * tree_index + 2, mid, right)

        self.segment_tree[tree_index] = self.segment_tree[2 * tree_index + 1] + self.segment_tree[2 * tree_index + 2]

    def _search_tree(self, tree_index, left, right, i, j):

        if (left == i & right == j):
            return self.segment_tree[tree_index]

        mid = left + ((right - left) // 2)

        if (i > mid):
            return self._search_tree(2 * tree_index + 1, left, mid, i, j)
        elif (j <= mid):
            return self._search_tree(2 * tree_index + 2, mid, right)
        

