import collections


class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:

        road_set_dic = collections.defaultdict(set)
        road_dic = collections.defaultdict(list)
        for city_1, city_2 in roads:
            road_dic[city_1].append(city_2)
            road_dic[city_2].append(city_1)

            road_set_dic[city_1].add(city_2)
            road_set_dic[city_2].add(city_1)

        edit_distance_list = [[0 for _ in range(len(names))] for _ in range(len(targetPath))]

        for step, target in enumerate(targetPath):

            for num in range(len(names)):

                cur_name = names[num]

                addition = 1
                if target == cur_name:
                    addition = 0

                if step == 0:
                    edit_distance_list[step][num] += addition
                else:
                    ingress_list = road_dic[num]

                    min_edit = float("inf")
                    for ingress in ingress_list:
                        edit_distance = edit_distance_list[step - 1][ingress]
                        min_edit = min(min_edit, edit_distance)

                    edit_distance_list[step][num] = min_edit + addition

        res_path = []
        prev_loc = -1

        for step in range(len(targetPath) - 1, -1, -1):

            cur_row = edit_distance_list[step]

            res = -1
            min_edit_distance = float("inf")
            for index, edit_distance in enumerate(cur_row):
                if edit_distance < min_edit_distance:

                    if step == len(targetPath) - 1:
                        res = index
                        min_edit_distance = edit_distance
                    else:
                        reachable_locations = road_set_dic[index]
                        if prev_loc in reachable_locations:
                            res = index
                            min_edit_distance = edit_distance

            res_path.append(res)
            prev_loc = res

        return res_path[::-1]
