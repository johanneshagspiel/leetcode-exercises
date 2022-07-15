import math
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        array_1 = nums1[:m]
        pointer_1 = 0
        pointer_2 = 0
        pointer_3 = 0

        while pointer_3 < (m + n):

            if pointer_1 < m:
                value_1 = array_1[pointer_1]
            else:
                value_1 = math.inf

            if pointer_2 < n:
                value_2 = nums2[pointer_2]
            else:
                value_2 = math.inf

            if value_1 < value_2:
                pointer_1+=1
            else:
                pointer_2+=1

            nums1[pointer_3] = min(value_1, value_2)
            pointer_3 += 1
        