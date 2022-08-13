class UndergroundSystem:

    def __init__(self):
        self.ride_id = 0
        self.in_station_dic = {}
        self.out_station_dic = {}
        self.ongoing_ride_dic = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:

        if stationName not in self.in_station_dic:
            self.in_station_dic[stationName] = {}

        ride_number = self.ride_id
        self.ride_id += 1

        self.in_station_dic[stationName][ride_number] = t

        self.ongoing_ride_dic[id] = ride_number


    def checkOut(self, id: int, stationName: str, t: int) -> None:

        if stationName not in self.out_station_dic:
            self.out_station_dic[stationName] = {}

        ride_number = self.ongoing_ride_dic.pop(id)

        self.out_station_dic[stationName][ride_number] = t


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        in_dic = self.in_station_dic[startStation]
        out_dic = self.out_station_dic[endStation]

        time_list = []

        for ride_number, start_time in in_dic.items():
            if ride_number in out_dic:
                end_time = out_dic[ride_number]
                duration = end_time - start_time
                time_list.append(duration)

        avg = sum(time_list) / len(time_list)
        return avg
