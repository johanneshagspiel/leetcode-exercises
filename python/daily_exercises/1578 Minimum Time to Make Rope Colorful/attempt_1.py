from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        n = len(colors)
        res = 0

        def check_range(range_start, range_end, skip_index):

            nonlocal res

            for index in range(range_start, range_end + 1):
                if index != skip_index:
                    res += neededTime[index]

        previous_color = None
        previous_color_start = None
        max_time = None
        max_time_index = None


        for index in range(n):
            current_color = colors[index]
            current_time = neededTime[index]

            if current_color != previous_color:
                if previous_color != None:
                    check_range(previous_color_start, index - 1, max_time_index)

                previous_color = current_color
                max_time = current_time
                previous_color_start = index
                max_time_index = index

            else:
                if current_time > max_time:
                    max_time = current_time
                    max_time_index = index

        check_range(previous_color_start, n - 1, max_time_index)
        return res