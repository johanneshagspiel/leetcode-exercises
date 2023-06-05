from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        previous = [1]

        if rowIndex == 0:
            return previous

        else:

            for row in range(1, rowIndex+1):
                current = [1 for _ in range(row + 1)]

                for position in range(1, row):
                    current[position] = previous[position] + previous[position-1]

                previous = current

            return previous

