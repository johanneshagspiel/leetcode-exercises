class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        dp = [startFuel] + ([0] * len(stations))

        for index, (location, capacity) in enumerate(stations):

            for prev in range(index, -1, -1):
                if dp[prev] >= location:
                    dp[prev + 1] = max(dp[prev + 1], dp[prev] + capacity)

        for station, reachable_lcoation in enumerate(dp):
            if reachable_lcoation >= target:
                return station

        return -1
