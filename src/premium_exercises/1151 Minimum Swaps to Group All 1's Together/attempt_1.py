import math
from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        number_of_ones = sum([number for number in data if number == 1])
        length_array = len(data)
        min_swaps = math.inf

        for start_index in range(0, length_array - number_of_ones + 1):
            swaps_needed = 0
            for index in range(start_index, start_index + number_of_ones):
                number_at_array = data[index]
                if number_at_array == 0:
                    swaps_needed += 1

            if swaps_needed < min_swaps:
                min_swaps = swaps_needed

        return min_swaps



