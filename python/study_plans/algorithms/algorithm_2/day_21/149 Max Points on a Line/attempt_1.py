import math
from decimal import Decimal, getcontext

from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distance_dic = {}

        max_points = 1

        for start_index in range(n):
            current_x, current_y = points[start_index]
            distance_dic[(current_x, current_y)] = {}

            other_points = points[:start_index] + points[(start_index + 1):]

            for other_x, other_y in other_points:
                distance_x, distance_y = other_x - current_x, other_y - current_y
                normalizing_factor = 1 / (math.sqrt((math.pow(distance_x, 2) + math.pow(distance_y, 2))))
                unit_distance_x, unit_distance_y = round(Decimal(normalizing_factor * distance_x), 9), round(
                    Decimal(normalizing_factor * distance_y), 9)

                if (unit_distance_x, unit_distance_y) in distance_dic[(current_x, current_y)]:
                    current_entry = distance_dic[(current_x, current_y)][(unit_distance_x, unit_distance_y)]
                    current_entry += 1
                    distance_dic[(current_x, current_y)][(unit_distance_x, unit_distance_y)] = current_entry
                    max_points = max(current_entry, max_points)

                else:
                    distance_dic[(current_x, current_y)][(unit_distance_x, unit_distance_y)] = 1

        return max_points

