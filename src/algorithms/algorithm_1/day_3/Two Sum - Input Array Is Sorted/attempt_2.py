import collections
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        len_numbers = len(numbers)

        for start_index, number in enumerate(numbers[:-1]):
            complement_number = target - number

            for compare_index in range(start_index + 1, len_numbers):
                number_two = numbers[compare_index]
                if number_two == complement_number:
                    return [start_index+1, compare_index+1]


if __name__ == '__main__':
    solution = Solution()

    input_1 = [0,0,3,4]
    target = 0
    output_1 = solution.twoSum(input_1, target)
    expected_output = [1,3,12,0,0]
    print(output_1)
