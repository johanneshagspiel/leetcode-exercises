import collections
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        list_to_pop = []
        original_length = len(nums)

        for index, number in enumerate(nums[:original_length]):
            if number == 0:
                nums.append(0)
                current_length_list_to_pop = len(list_to_pop)
                adjusted_index = index - current_length_list_to_pop
                list_to_pop.append(adjusted_index)

        for index_to_pop in list_to_pop:
            nums.pop(index_to_pop)

        print(nums)


if __name__ == '__main__':
    solution = Solution()

    input_1 = [0,1,0,3,12]
    output_1 = solution.moveZeroes(input_1)
    expected_output = [1,3,12,0,0]
    print(output_1)
