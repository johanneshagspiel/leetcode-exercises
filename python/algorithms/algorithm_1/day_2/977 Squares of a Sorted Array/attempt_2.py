import collections
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        dequeu_nums = collections.deque(nums)
        result_list = []

        while dequeu_nums:

            first_element = pow(dequeu_nums[0], 2)
            last_element = pow(dequeu_nums[-1], 2)

            if first_element > last_element:
                result_list.append(first_element)
                dequeu_nums.popleft()
            else:
                result_list.append(last_element)
                dequeu_nums.pop()

        return result_list[::-1]


if __name__ == '__main__':
    solution = Solution()

    input_1 = [-4,-1,0,3,10]
    output_1 = solution.sortedSquares(nums=input_1)
    print(output_1)
    expected_1 = [0,1,9,16,100]
