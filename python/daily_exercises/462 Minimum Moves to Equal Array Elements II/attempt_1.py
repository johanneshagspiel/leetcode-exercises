import copy
import math
from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        nums_copy = copy.deepcopy(nums)

        smallest = min(nums_copy)
        largest = max(nums_copy)

        count = 0

        for index, number in enumerate(nums_copy):

            if number == smallest:
                if number < largest:
                    nums_copy[index] += 1
                    count += 1
                    smallest += 1

            elif number == largest:
                if number > smallest:
                    nums_copy[index] -= 1
                    count += 1
                    largest -= 1

            else:
                distance_to_smallest = math.abs(smallest - number)
                distance_to_lagest = math.abs(largest - number)

                if distance_to_smallest < distance_to_lagest:
                    nums_copy[index] += 1
                    count += 1
                elif distance_to_lagest < distance_to_smallest:
                    nums_copy[index] += 1
                    count += 1

        return count