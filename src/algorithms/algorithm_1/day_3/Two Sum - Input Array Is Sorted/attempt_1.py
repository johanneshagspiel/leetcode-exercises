import collections
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_dic = {}

        for index, number in enumerate(numbers):
            numbers_dic[number] = index + 1

        for index, number in enumerate(numbers):
            complement_number = target - number
            if complement_number in numbers_dic:
                complement_index = numbers_dic[complement_number]
                return [index + 1, complement_index]

if __name__ == '__main__':
    solution = Solution()

    input_1 = [2,7,11,15]
    target = 9
    output_1 = solution.twoSum(input_1, target)
    expected_output = [1,3,12,0,0]
    print(output_1)
