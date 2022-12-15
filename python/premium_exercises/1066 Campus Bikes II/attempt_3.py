class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        mem_dic = {}

        def _assign(bike_array, cur_worker):
            key = (cur_worker, tuple(bike_array))

            if key in mem_dic:
                return mem_dic[key]

            if cur_worker == len(bike_array):
                return 0

            min_distance = float("inf")

            for j in range(len(bike_array)):
                if bike_array[j] == 0:
                    xw, yw = workers[cur_worker]
                    xb, yb = bikes[j]

                    bike_array[j] = 1

                    min_distance = min(min_distance, abs(xw - xb) + abs(yw - yb) + _assign(bike_array, cur_worker + 1))

                    bike_array[j] = 0

            mem_dic[key] = min_distance
            return min_distance

        bike_array = [0 for _ in range(len(bikes))]
        return _assign(bike_array, 0)
