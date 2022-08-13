import copy
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        N = len(nums)

        it = 1
        result_list = []

        start = [0 for _ in range(N)]
        stop = N-1

        current = copy.deepcopy(start)
        previous = copy.deepcopy(start)

        for i in range(N-1, -1, -1):
            for j in range(0 , N, 1):

                if i == (N-1):
                    if nums[j] > nums[i]:
                        current[j] += 1

                else:
                    if nums[j] > nums[i]:
                        current[j] = 1 + previous[j]
                    else:
                        current[j] = previous[j]

                if j == stop:
                    break

            result_list.append(current[N-it])
            it += 1
            stop -= 1

            previous = current
            current = copy.deepcopy(start)

        return result_list[::-1]
