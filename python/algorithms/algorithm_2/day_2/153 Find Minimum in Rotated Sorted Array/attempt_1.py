from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left_pointer = 0
        n = len(nums)
        right_pointer = n - 1

        lowest_number = min(nums[left_pointer], nums[right_pointer])

        while left_pointer <= right_pointer:
            pivot = left_pointer + ((right_pointer - left_pointer) // 2)
            pivot_value = nums[pivot]

            value_right = nums[right_pointer]
            value_left = nums[left_pointer]

            if pivot_value < lowest_number:
                right_pointer = pivot - 1
                lowest_number = pivot_value

            elif pivot_value > lowest_number:
                if value_right > value_left:
                    right_pointer = pivot - 1
                else:
                    left_pointer = pivot + 1

            elif pivot_value == lowest_number:
                break

        return lowest_number

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin([2,1]))