from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        total_length = m + n

        index_num_1 = 0
        index_num_2 = 0

        all_elements_1 = m == 0

        for final_index in range(0, total_length):

            value_1 = nums1[index_num_1]

            if len(nums2) > index_num_2:
                value_2 = nums2[index_num_2]
            else:
                value_2 = 9999999999999999999999999999999999999999999999

            if value_2 < value_1 or all_elements_1:
                nums1.insert(final_index, value_2)
                nums1.pop()

                index_num_2 = index_num_2 + 1

            else:
                m = m - 1
                all_elements_1 = m == 0

            index_num_1 = index_num_1 + 1

        print(nums1)


if __name__ == '__main__':
    solution = Solution()

    input_1 = [1]
    input_1_size = 1
    input_2 = []
    input_2_size = 0
    output_1 = solution.merge(input_1, input_1_size, input_2, input_2_size)

    print(output_1)