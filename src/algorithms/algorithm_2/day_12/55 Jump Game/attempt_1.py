from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums) - 1

        def back_tracking(current_index):

            if current_index >= n:
                return True
            else:
                available_jumps = nums[current_index]
                if available_jumps == 0:
                    return False
                else:

                    for jump in range(1, available_jumps + 1):
                        current_index = current_index + jump
                        reach_final = back_tracking(current_index)

                        if reach_final:
                            return True

                        current_index = current_index - jump

                return False

        return back_tracking(0)


