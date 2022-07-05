from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:

        up = 1
        down = 0
        peak = 1

        result = 1
        n = len(ratings)

        for index in range(1, n):

            if ratings[index] > ratings[index-1]:
                up += 1
                peak = up
                down = 0
                result += up

            elif ratings[index] == ratings[index-1]:
                up = 1
                peak = 0
                down = 0
                result += 1

            else:
                down += 1
                result += down
                up = 1
                
                if down >= peak:
                    result += 1

        return result