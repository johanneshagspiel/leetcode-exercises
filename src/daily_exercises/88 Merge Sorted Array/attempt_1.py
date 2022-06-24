from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums_m = nums1[:m]

        index_1 = 0
        index_2 = 0
        total_index = 0

        while index_1 != m and index_2 != n:
            val_1 = nums_m[index_1]
            val_2 = nums2[index_2]

            if val_1 < val_2:
                nums1[total_index] = val_1
                index_1 += 1
            else:
                nums1[total_index] = val_2
                index_2 += 1

            total_index += 1

        if index_1 < m:
            nums1[total_index:] = nums_m[index_1:]

        if index_2 < n:
            nums_m[total_index:] = nums2[index_2:]
