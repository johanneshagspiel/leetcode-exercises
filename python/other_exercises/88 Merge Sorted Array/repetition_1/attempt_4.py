from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        array2_pointer = n - 1
        array1_pointer = m - 1
        combined_pointer = m + n - 1

        while array2_pointer >= 0 and array1_pointer >= 0:
            if nums1[array1_pointer] < nums2[array2_pointer]:
                nums1[combined_pointer] = nums2[array2_pointer]
                array2_pointer -= 1
            else:
                nums1[combined_pointer] = nums1[array1_pointer]
                array1_pointer -= 1

            combined_pointer -= 1

        while array2_pointer >= 0:
            nums1[combined_pointer] = nums2[array2_pointer]
            array2_pointer -= 1
            combined_pointer -= 1

        return nums1

