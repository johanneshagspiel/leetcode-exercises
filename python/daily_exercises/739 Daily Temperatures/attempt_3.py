class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dp = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures) - 2, -1, -1):
            current_temperature = temperatures[i]
            found = False

            for j in range(i + 1, len(temperatures), + 1):
                other_temperature = temperatures[j]

                if other_temperature > current_temperature:
                    dp[i] = j - i
                    found = True
                    break

            if not found:
                dp[i] = 0

        return dp


