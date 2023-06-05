from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False

        self.found = False

        def found(left, right):

            if not self.found:

                while left < right:
                    left_val = nums[left]
                    right_val = nums[right]

                    if left_val > right_val:
                        found(left + 1, right)
                        found(left, right - 1)

                    else:
                        pivot = left + ((right - left) // 2)

                        if pivot != left and pivot != right:

                            pivot_val = nums[pivot]

                            if left_val < pivot_val < right_val:
                                self.found = True
                            else:
                                found(left + 1, right)
                                found(left, right - 1)

        N = len(nums)

        left = 0
        right = N - 1

        found(left, right)
        return self.found
        