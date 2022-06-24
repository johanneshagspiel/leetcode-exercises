import math
from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        number_of_ones = sum([number for number in data if number == 1])
        min_swaps = math.inf

        swap_sum = 0

        for index, number in enumerate(data):
            if index < number_of_ones:
                if number == 0:
                    swap_sum += 1
            else:
                if swap_sum < min_swaps:
                    min_swaps = swap_sum

                last_entry = data[index - number_of_ones]
                if last_entry == 0:
                    swap_sum -= 1

                if number == 0:
                    swap_sum += 1

        if swap_sum < min_swaps:
            min_swaps = swap_sum

        return min_swaps
