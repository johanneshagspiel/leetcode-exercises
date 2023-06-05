from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_side = 0
        right_side = len(nums) - 1

        while left_side <= right_side:

            pivot = left_side + ((right_side - left_side) // 2)
            pivot_value = nums[pivot]

            if pivot_value == target:
                return pivot
            elif pivot_value < target:
                left_side = pivot + 1
            else:
                right_side = pivot - 1

        return -1




if __name__ == '__main__':
    solution = Solution()

    input_1 = [-1,0,3,5,9,12]
    t = 9
    output_1 = solution.search(input_1, t)
    print(output_1)
