from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        station_dic = {}
        for location, tank in stations:
            station_dic[location] = tank


        def rec_mem(current_position, current_tank, mem_dic):

            if current_position + current_tank >= target:
                return 0

            elif current_position in mem_dic:
                return mem_dic[current_position]

            else:

                station_list = []

                for reachable_location in range(current_position + 1, current_position + current_tank + 1):
                    if reachable_location in station_dic:

                        distance = reachable_location - current_position
                        tank_at_location = station_dic[reachable_location]
                        new_tank = current_tank - distance + tank_at_location

                        station_needed = 1 + rec_mem(reachable_location, new_tank, mem_dic)
                        station_list.append(station_needed)

                if len(station_list) == 0:
                    res = float("inf")
                else:
                    res = min(station_list)
                mem_dic[current_position] = res
                return res

        res = rec_mem(0, startFuel, {})

        return res if res != float("inf") else -1
