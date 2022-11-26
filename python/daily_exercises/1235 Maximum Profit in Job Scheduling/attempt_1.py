class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        combined = list(zip(startTime, endTime, profit))
        combined.sort(key=lambda x: x[0])

        startTime = [x[0] for x in combined]
        endTime = [x[1] for x in combined]
        profit = [x[2] for x in combined]

        jobs = len(startTime)
        dp = [0] * jobs

        for i in range(jobs - 1, -1, -1):

            left = i + 1
            right = jobs - 1

            j = -1

            while left <= right:
                pivot = left + ((right - left) // 2)

                if startTime[pivot] >= endTime[i]:
                    j = pivot
                    right = pivot - 1
                else:
                    left = pivot + 1

            if j == -1:
                cur_profit = profit[i]
            else:
                cur_profit = profit[i] + dp[j]

            if i == (jobs - 1):
                dp[i] = cur_profit
            else:
                dp[i] = max(cur_profit, dp[i + 1])

        return dp[0]
