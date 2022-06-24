from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result_list = []
        n = len(candidates)

        def back_tracking(remaining, current_list, start_index):

            if remaining == 0:
                result_list.append(current_list[::])
                return

            for index in range(start_index, n):

                if index > start_index and candidates[index] == candidates[index - 1]:
                    continue

                if remaining - candidates[index] < 0:
                    break

                current_list.append(candidates[index])
                back_tracking(remaining - candidates[index], current_list, index + 1)
                current_list.pop()

        back_tracking(target, [], 0)
        return result_list