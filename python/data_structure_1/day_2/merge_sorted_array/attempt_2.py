from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1

        nums1[:n] = nums2[:n]


if __name__ == '__main__':
    solution = Solution()

    input_1 = [1]
    input_1_size = 1
    input_2 = []
    input_2_size = 0
    output_1 = solution.merge(input_1, input_1_size, input_2, input_2_size)

    print(output_1)