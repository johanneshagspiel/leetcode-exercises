class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        distance_dic = {}

        for start_index in range(n):
            current_x, current_y = points[start_index]
            distance_dic[(current_x, current_y)] = {}

            other_points = points[:start_index] + points[(start_index + 1):]

            for other_x, other_y in other_points:
                distance_x, distance_y = other_x - current_x, other_y - current_y
                normalizing_factor = 1 / (math.sqrt((math.pow(distance_x, 2) + math.pow(distance_y, 2))))
                unit_distance_x, unit_distance_y = normalizing_factor * distance_x, normalizing_factor * distance_y

                if (unit_distance_x, unit_distance_y) in distance_dic[(current_x, current_y)]:
                    distance_dic[(current_x, current_y)][(unit_distance_x, unit_distance_y)] = 0
                else:
                    distance_dic[(current_x, current_y)][(unit_distance_x, unit_distance_y)] += 1

        max_points = 1

        for current_key, other_distance_dic in distance_dic.items():

            for move_vector, location_count in other_distance_dic.items():
                current_points = 1 + location_count
                max_points = max(current_points, max_points)

        return max_points