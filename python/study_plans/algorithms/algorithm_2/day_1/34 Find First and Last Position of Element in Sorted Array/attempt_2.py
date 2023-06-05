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
                if pivot == 0:
                    right_position = self.binary_search_right(nums, target)
                    return [pivot, right_position]
                elif nums[pivot - 1] != target:
                    right_position = self.binary_search_right(nums, target)
                    return [pivot, right_position]
                else:
                    last_pointer = pivot - 1

        return [-1, -1]


    def binary_search_right(self, nums, target):

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
                if pivot == 0:
                    return pivot
                elif nums[pivot + 1] != target:
                    return pivot
                else:
                    first_pointer = pivot + 1
