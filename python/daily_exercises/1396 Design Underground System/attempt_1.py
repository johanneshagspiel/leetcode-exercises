import collections


class UndergroundSystem:

    def __init__(self):
        self.current_passengers_dic = {}
        self.average_time_dic = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.current_passengers_dic[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station_name, start_time = self.current_passengers_dic.pop(id)

        if (start_station_name, stationName) not in self.average_time_dic:
            self.average_time_dic[(start_station_name, stationName)] = (0, 0)

        current_time, current_count = self.average_time_dic[(start_station_name, stationName)]
        current_time += (t - start_time)
        current_count += 1

        self.average_time_dic[(start_station_name, stationName)] = current_time, current_count

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        current_time, current_count = self.average_time_dic[(startStation, endStation)]
        return current_time / current_count
