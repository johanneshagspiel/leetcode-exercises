from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        n = len(nums)
        num_violations = 0

        previous_number = nums[0]
        previous_previous_number = None

        for index in range(1, n):
            current_number = nums[index]

            if previous_number > current_number:

                num_violations += 1

                if num_violations == 2:
                    return False

                if index == 1:
                    previous_number = current_number
                    previous_previous_number = current_number
                else:
                    if previous_previous_number <= current_number:
                        previous_number = current_number
                        previous_previous_number = previous_number
                    else:
                        previous_number = previous_number
                        previous_previous_number = previous_number

            else:
                previous_previous_number = previous_number
                previous_number = current_number

        return True
