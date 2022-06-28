from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        n = len(nums)

        if n <= 2:
            return True
        else:

            previous_previous_number = None
            previous_number = nums[0]

            found_change = False

            for index in range(1, n):
                compare_number = nums[index]
                if previous_number > compare_number:
                    if found_change:
                        return False
                    else:
                        found_change = True
                        if index == 1:
                            previous_number = compare_number
                        else:
                            previous_previous_number = previous_number

                            if previous_previous_number <= compare_number:
                                previous_number = compare_number
                            else:
                                previous_number = previous_number
                else:
                    previous_previous_number = previous_number
                    previous_number = compare_number



            return True


