from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()

        max_height = 0

        for index in range(1, len(horizontalCuts)):
            height = horizontalCuts[index] - horizontalCuts[index - 1]
            max_height = max(height, max_height)

        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()

        max_width = 0

        for index in range(1, len(verticalCuts)):
            width = verticalCuts[index] - verticalCuts[index-1]
            max_width = max(width, max_width)

        result = (max_width * max_height) % (pow(10,9) + 7)
        return result
