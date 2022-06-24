import collections
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        norm_k = k % len(nums)
        nums[:] = nums[-norm_k:] + nums[:-norm_k]

        print(nums)

if __name__ == '__main__':
    solution = Solution()

    input_1 = [1,2,3,4,5,6,7]
    k_1 = 3
    #output_1 = solution.rotate(input_1, k_1)
    expected_1 = [5,6,7,1,2,3,4]

    test = 3 % 6
    print(input_1[3:])
