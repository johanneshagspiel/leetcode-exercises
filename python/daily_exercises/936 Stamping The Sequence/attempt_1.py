from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:

        num_options = len(target) - len(stamp) + 1

        dp = [["?"]*len(target) for _ in range(num_options)]

        shift = 0
        for row in range(num_options):

            letter_index = 0
            for column in range(len(target)):

                if column >= shift:
                    dp[row][column] = stamp[letter_index]
                    letter_index += 1
                    if letter_index == len(stamp):
                        break

            shift += 1

        leftmost_index = []

        target_index = 0



        return dp
