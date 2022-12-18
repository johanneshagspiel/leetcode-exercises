class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        dp = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures) - 1, -1, -1):
            left = i + 1
            right = len(temperatures) - 1
            found = False

            while left < right:
                pivot = left + ((right - left) // 2)

                if temperatures[i] < temperatures[pivot]:
                    right = pivot
                    found = True
                else:
                    left = pivot + 1

            if found:
                wait = right - i
                dp[i] = wait
            else:
                dp[i] = 0

        return dp