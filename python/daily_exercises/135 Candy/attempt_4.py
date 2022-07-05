from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:

        up = 1
        down = 0
        peak = 0

        result = 1

        n = len(ratings)

        for index in range(1, n):
            if ratings[index] > ratings[index-1]:
                up += 1
                peak = up
                down = 0
                result += up

            elif ratings[index] == ratings[index-1]:
                result += 1
                up = down = peak = 0

            else:
                down += 1
                up = 0
                result += down

                if down >= peak:
                    result += 1

        return result