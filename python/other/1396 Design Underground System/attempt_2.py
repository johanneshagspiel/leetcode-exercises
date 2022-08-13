class UndergroundSystem:

    def __init__(self):
        self.started_rides = {}
        self.ride_dic = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.started_rides[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_name, start_time = self.started_rides.pop(id)
        duration = t - start_time

        if (start_name, stationName) in self.ride_dic:
            total_duration, ride_count = self.ride_dic[(start_name, stationName)]
            total_duration += duration
            ride_count += 1
            self.ride_dic[(start_name, stationName)] = total_duration, ride_count
        else:
            self.ride_dic[(start_name, stationName)] = duration, 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_duration, ride_count = self.ride_dic[(startStation, endStation)]
        return total_duration / ride_count
