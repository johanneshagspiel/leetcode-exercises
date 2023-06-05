import math
from decimal import Decimal
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 1

        distance_dic = {}
        n = len(points)
        max_points = 2

        for start_index in range(n):
            current_x, current_y = points[start_index]
            distance_dic[(current_x, current_y)] = {}

            for end_index in range(start_index + 1, n):
                other_x, other_y = points[end_index]
                distance_x, distance_y = other_x - current_x, other_y - current_y
                normalization_factor = 1 / (math.sqrt((math.pow(distance_x, 2) + math.pow(distance_y, 2))))

                normalized_x, normalized_y = round(Decimal(normalization_factor * distance_x), 9), round(Decimal(normalization_factor * distance_y), 9)

                if (normalized_x, normalized_y) in distance_dic[(current_x, current_y)]:
                    current_entry = distance_dic[(current_x, current_y)][(normalized_x, normalized_y)]
                    current_entry += 1
                    distance_dic[(current_x, current_y)][(normalized_x, normalized_y)] = current_entry
                else:
                    current_entry = 2
                    distance_dic[(current_x, current_y)][(normalized_x, normalized_y)] = current_entry

                max_points = max(max_points, current_entry)

        return max_points
