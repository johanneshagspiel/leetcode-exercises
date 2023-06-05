import math


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        coordinates.sort()

        start_x, start_y = coordinates[0]
        second_x, second_y = coordinates[1]

        compare_x_delta = second_x - start_x
        compare_y_delta = second_y - start_y
        magnitude = math.sqrt(pow(compare_x_delta, 2) + pow(compare_y_delta, 2))
        unit_x_delta = compare_x_delta / magnitude
        unit_y_delta = compare_y_delta / magnitude

        for compare_x, comapare_y in coordinates[2:]:
            x_delta = compare_x - start_x
            y_delta = comapare_y - start_y

            if not unit_x_delta or not unit_y_delta:
                if not unit_x_delta:
                    if unit_x_delta != x_delta:
                        return False

                if not unit_y_delta:
                    if unit_y_delta != y_delta:
                        return False

            else:
                x_delta_multiple = x_delta / unit_x_delta
                y_delta_multiple = y_delta / unit_y_delta

                if f"{x_delta_multiple:.3f}" != f"{y_delta_multiple:.3f}":
                    return False

        return True
