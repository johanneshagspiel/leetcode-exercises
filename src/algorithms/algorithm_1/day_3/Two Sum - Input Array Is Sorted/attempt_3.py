import collections
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        first_entry = 0
        last_entry = len(numbers) - 1

        while first_entry < last_entry:
            low_number = numbers[first_entry]
            high_number = numbers[last_entry]

            combination = low_number + high_number

            if combination == target:
                return [first_entry + 1, last_entry + 1]
            elif combination < target:
                first_entry += 1
            else:
                last_entry -= 1

        return [-1, -1]


if __name__ == '__main__':
    solution = Solution()

    input_1 = [0,0,3,4]
    target = 0
    output_1 = solution.twoSum(input_1, target)
    expected_output = [1,3,12,0,0]
    print(output_1)
