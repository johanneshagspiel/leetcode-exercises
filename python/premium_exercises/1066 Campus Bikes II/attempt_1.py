class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        n = len(workers)
        m = len(bikes)

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            xw = workers[i][0]
            yw = workers[i][1]

            for j in range(m):
                xb = bikes[j][0]
                yb = bikes[j][1]

                manhattan_distance = abs(xw - xb) + abs(yw - yb)

                dp[i][j] = manhattan_distance

        min_distance = 999999999
        mem_dic = {}

        def get_min_distance(row, cur_distance, col_set):
            nonlocal min_distance

            if row == n:
                min_distance = min(min_distance, cur_distance)

            else:
                distance_array = dp[row]

                for i in range(m):
                    if i not in col_set:
                        cur_distance += distance_array[i]
                        col_set.add(i)

                        get_min_distance(row + 1, cur_distance, col_set)

                        col_set.remove(i)
                        cur_distance -= distance_array[i]

        get_min_distance(0, 0, set())

        return min_distance
