class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        dp = [0 for _ in range(len(temperatures))]

        heap = [(temperatures[-1], 0)]
        count = 1
        found = False

        for i in range(len(temperatures) - 2, -1, -1):

            current_temperature = temperatures[i]
            dif = -1

            for temperature, index in heap:
                if temperature > current_temperature:
                    dif = count - index
                    break

            if dif == -1:
                dp[i] = 0
            else:
                if found:
                    dp[i] = dif
                else:
                    dp[i] = 1
                    found = True

            heap.append((current_temperature, count))
            heap.sort(key=lambda x: x[0], reverse=False)
            count += 1

        return dp