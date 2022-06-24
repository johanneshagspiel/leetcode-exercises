from typing import List

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            pivot = left + ((right - left) // 2)
            pivot_value = nums[pivot]

            if pivot_value == target:
                return pivot

            elif pivot_value < target:
                left = pivot + 1

            elif pivot_value > target:
                right = pivot - 1

        return left

if __name__ == '__main__':
    solution = Solution()

    input_1 = [1,3,5,6]
    target_1 = 5
    output_1 = solution.searchInsert(nums=input_1, target=target_1)
    expected_1 = 2

    # print(1)
    # print(output_1)
    # print(output_1 == expected_1)
    # print(" ")


    input_2 = [1,3,5,6]
    target_2 = 2
    output_2 = solution.searchInsert(input_2, target_2)
    expected_2 = 1

    print(2)
    print(output_2)
    print(output_2 == expected_2)
    print(" ")
    #
    # input_3 = [-1,0,3,5,9,12]
    # target_3 = 12
    # output_3 = solution.search(input_3, target_3)
    # expected_3 = 5
    #
    # print(3)
    # print(output_3)
    # print(output_3 == expected_3)
    # print(" ")
