from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        first_pointer = 0
        last_pointer = n - 1

        while first_pointer <= last_pointer:

            pivot = first_pointer + (last_pointer - first_pointer)
            pivot_value = nums[pivot]

            if pivot_value < target:
                first_pointer = pivot + 1

            if pivot_value > target:
                last_pointer = pivot - 1

            if pivot_value == target:

                first_pointer = pivot
                while True:
                    value_at_first_pointer = nums[first_pointer]
                    if value_at_first_pointer == target:
                        first_pointer -= 1
                        if first_pointer < 0:
                            first_pointer += 1
                            break
                    else:
                        first_pointer += 1
                        break

                last_pointer = pivot
                while True and last_pointer < n:
                    value_at_last_pointer = nums[last_pointer]
                    if value_at_last_pointer == target:
                        last_pointer += 1
                        if first_pointer == n:
                            last_pointer -= 1
                            break
                    else:
                        last_pointer -= 1
                        break

                return [first_pointer, last_pointer]

        return [-1, -1]

if __name__ == "__main__":
    solution = Solution()
    solution.searchRange(nums=[1], target=1)