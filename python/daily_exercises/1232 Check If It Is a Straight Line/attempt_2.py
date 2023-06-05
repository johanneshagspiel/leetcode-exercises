import math


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        start_x, start_y = coordinates[0]
        second_x, second_y = coordinates[1]

        x_delta = second_x - start_x
        y_delta = second_y - start_y

        magnitude = math.sqrt(pow(x_delta, 2) + pow(y_delta, 2))

        unit_x_delta = round(x_delta / magnitude, 4)
        unit_y_delta = round(y_delta / magnitude, 4)

        negative_unit_x_delta = (-1) * unit_x_delta
        negative_unit_y_delta = (-1) * unit_y_delta

        delta_set = set()
        delta_set.add((unit_x_delta, unit_y_delta))
        delta_set.add((negative_unit_x_delta, negative_unit_y_delta))

        for compare_x, comapare_y in coordinates[2:]:
            x_delta = compare_x - start_x
            y_delta = comapare_y - start_y

            magnitude = math.sqrt(pow(x_delta, 2) + pow(y_delta, 2))

            unit_x_delta = round(x_delta / magnitude, 4)
            unit_y_delta = round(y_delta / magnitude, 4)

            if (unit_x_delta, unit_y_delta) not in delta_set:
                return False

        return True
