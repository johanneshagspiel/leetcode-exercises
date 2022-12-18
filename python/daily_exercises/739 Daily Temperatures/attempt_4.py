class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        ans = [0] * n
        hottest = 0

        for i in range(n - 1, -1, -1):
            current_temperature = temperatures[i]

            if current_temperature >= hottest:
                hottest = current_temperature
                continue

            days = 1
            while temperatures[i + days] <= current_temperature:
                days += ans[i + days]
            ans[i] = days

        return ans
