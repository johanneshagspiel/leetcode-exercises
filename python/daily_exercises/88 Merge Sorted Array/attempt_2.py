from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        pointer_1 = m - 1
        pointer_2 = n - 1
        pointer_3 = (m + n) - 1

        while pointer_3 >= 0:

            if pointer_2 < 0:
                break

            if pointer_1 >= 0 and (nums1[pointer_1] > nums2[pointer_2]):
                nums1[pointer_3] = nums1[pointer_1]
                pointer_1 -= 1
            else:
                nums1[pointer_3] = nums2[pointer_2]
                pointer_2 -= 1
            pointer_3 -= 1
