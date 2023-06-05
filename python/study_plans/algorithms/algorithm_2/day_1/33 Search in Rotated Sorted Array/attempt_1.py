from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        left_pointer = 0
        right_pointer = n - 1

        first_value = nums[0]

        while left_pointer <= right_pointer:

            pivot = left_pointer + ((right_pointer - left_pointer) // 2)
            pivot_value = nums[pivot]

            if pivot_value == target:
                return pivot

            else:
                if pivot_value >= first_value:

                    if pivot_value > target:
                        right_pointer = pivot - 1

                    if pivot_value < target:
                        left_pointer = pivot + 1

                else:
                    if pivot_value > target:
                        left_pointer = pivot + 1

                    if pivot_value < target:
                        right_pointer = pivot - 1


if __name__ == "__main__":
    solution = Solution()
    solution.search(nums = [4,5,6,7,0,1,2], target = 0)