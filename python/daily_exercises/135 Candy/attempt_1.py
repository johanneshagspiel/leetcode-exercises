import copy
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:

        previous = 1
        count = 0

        below_0 = False
        right_most_below_index = -1

        n = len(ratings)

        for index in range(1, n):
            if ratings[index] > ratings[index - 1]:
                previous += 1
                count += previous
            elif ratings[index] == ratings[index - 1]:
                count += previous
            else:
                if ratings[index - 1] <= 1:
                    previous = ratings[index - 1] - 1
                else:
                    previous = 1
                count += previous

                if previous <= 0:
                    below_0 = True
                    right_most_below_index = index


        return count

