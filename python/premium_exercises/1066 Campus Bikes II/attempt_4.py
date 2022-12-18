class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        mem_dic = {}

        def _assign(cur_worker, bike_array):
            key = (cur_worker, tuple(bike_array))

            if key in mem_dic:
                return mem_dic[key]

            elif cur_worker == len(workers):
                return 0

            else:

                min_distance = float("inf")

                xw, yw = workers[cur_worker]

                for j in range(len(bike_array)):
                    if bike_array[j] == 0:
                        bike_array[j] = 1

                        xb, yb = bikes[j]

                        min_distance = min(min_distance, abs(xw - xb) + abs(yw - yb) + _assign(cur_worker + 1, bike_array))

                        bike_array[j] = 0

                mem_dic[key] = min_distance
                return min_distance

        return _assign(0, [0 for _ in range(len(bikes))])
