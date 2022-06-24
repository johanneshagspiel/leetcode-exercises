from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        min_number = 0
        max_number = len(nums)

        total_number_array = set(list(range(min_number, max_number + 1)))
        nums_set = set(nums)

        missing_value = total_number_array - nums_set

        return missing_value.pop()

if __name__ == '__main__':
    solution = Solution()

    input_1 = [9,6,4,2,3,5,7,0,1]
    output_1 = solution.missingNumber(input_1)
    expected_1 = 8

    print(output_1)