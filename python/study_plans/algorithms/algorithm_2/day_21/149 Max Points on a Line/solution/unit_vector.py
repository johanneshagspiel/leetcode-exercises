import math
from decimal import Decimal
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 1

        n = len(points)
        distance_dic = {}
        max_points = 2

        for point_index in range(n):
            current_x, current_y = points[point_index]
            other_points = points[:point_index] + points[(point_index + 1):]
            distance_dic[(current_x, current_y)] = {}

            for other_x, other_y in other_points:
                distance_x, distance_y = other_x - current_x, other_y - current_y

                normalization_factor = 1 / (math.sqrt((math.pow(distance_x, 2) + math.pow(distance_y , 2))))

                normalized_z, normalized_y = round(Decimal(distance_x * normalization_factor), 9), round(Decimal(distance_y * normalization_factor), 9)

                if (normalized_z, normalized_y) in distance_dic[(current_x, current_y)]:
                    current_entry = distance_dic[(current_x, current_y)][(normalized_z, normalized_y)]
                    current_entry += 1
                    distance_dic[(current_x, current_y)][(normalized_z, normalized_y)] = current_entry
                else:
                    current_entry = 2
                    distance_dic[(current_x, current_y)][(normalized_z, normalized_y)] = current_entry

                max_points = max(max_points, current_entry)

        return max_points

