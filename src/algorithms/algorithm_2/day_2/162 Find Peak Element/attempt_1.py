from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        found_peak, peak_index = self.binary_search(nums)
        if found_peak:
            return peak_index
        else:
            return -1

    def binary_search(self, nums):
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            pivot = left_pointer + ((right_pointer - left_pointer) // 2)
            pivot_value = nums[pivot]

            if pivot == 0:
                next_value = nums[pivot + 1]
                if next_value < pivot_value:
                    return False, -1
                else:
                    return True, 0
            if pivot == (len(nums) - 1):
                previous_value = nums[pivot - 1]
                if previous_value < pivot_value:
                    return True, pivot
                else:
                    return False, -1

            previous_value = nums[pivot - 1]
            next_value = nums[pivot + 1]

            if pivot_value > previous_value and pivot_value > next_value:
                return True, pivot
            elif pivot > previous_value and pivot_value < next_value:
                left_pointer = pivot
            elif pivot < previous_value and pivot_value > next_value:
                right_pointer = pivot

            else:
                found_left, peak_index = self.binary_search(nums[:pivot])
                if found_left:
                    return True, peak_index
                found_right, peak_index = self.binary_search(nums[pivot:])
                if found_right:
                    return True, pivot + peak_index
                else:
                    return False, -1

        return False, -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.findPeakElement([1,2,3,1]))