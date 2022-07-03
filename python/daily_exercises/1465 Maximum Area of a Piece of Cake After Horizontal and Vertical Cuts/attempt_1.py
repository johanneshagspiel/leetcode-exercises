from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()

        max_horizontal_cut = 0

        for start_index in range(1, len(horizontalCuts)):
            distance = horizontalCuts[start_index] - horizontalCuts[start_index-1]
            max_horizontal_cut = max(max_horizontal_cut, distance)

        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()

        max_vertical_cut = 0

        for start_index in range(1, len(verticalCuts)):
            distance = verticalCuts[start_index] - verticalCuts[start_index-1]
            max_vertical_cut = max(max_vertical_cut, distance)


        result = (max_horizontal_cut * max_vertical_cut) % ((pow(10, 9) + 7))
        return result
