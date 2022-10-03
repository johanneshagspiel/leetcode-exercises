class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        total_time = 0
        current_max_time = 0
        n = len(colors)

        for index in range(n):

            if index != 0 and colors[index - 1] != colors[index]:
                current_max_time = 0

            total_time += min(current_max_time, neededTime[index])
            current_max_time = max(current_max_time, neededTime[index])

        return total_time
