import math
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:

        min_count = math.inf
        n = len(ratings)

        def back_track(index, current_count, current_position):

            if index == n:
                min_count = min(min_count, current_count)
                return

            elif current_position <= 0:
                return

            else:
                if ratings[index] < ratings[index - 1]:
                    back_track(index + 1, current_count + current_position, 1)
                    back_track(index + 1, current_count + current_position, current_position - 1)

                elif ratings[index] == ratings[index - 1]:
                    back_track(index + 1, current_count + current_position, current_position)

                else:
                    back_track(index + 1, )
