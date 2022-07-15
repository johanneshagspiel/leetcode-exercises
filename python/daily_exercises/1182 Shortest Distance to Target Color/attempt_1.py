from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:

        n = len(colors)

        dp_right = [[-1] * n for _ in range(3)]

        last_color = colors[-1]
        for color in range(1, 4):
            if color == last_color:
                dp_right[color - 1][-1] = 0

        for position in range(n - 2, -1, -1):
            current_color = colors[position]

            for color in range(1, 4):
                if color == current_color:
                    dp_right[color - 1][position] = 0
                else:
                    if dp_right[color - 1][position + 1] == -1:
                        dp_right[color - 1][position] = -1
                    else:
                        dp_right[color - 1][position] = 1 + dp_right[color - 1][position + 1]


        dp_left = [[-1] * n for _ in range(3)]

        first_color = colors[0]
        for color in range(1, 4):
            if color == first_color:
                dp_left[color - 1][0] = 0

        for position in range(1, n):
            current_color = colors[position]

            for color in range(1, 4):
                if color == current_color:
                    dp_left[color-1][position] = 0
                else:
                    if dp_left[color-1][position-1] == -1:
                        dp_left[color - 1][position] = -1
                    else:
                        dp_left[color - 1][position] = 1 + dp_left[color-1][position-1]


        result_list = []

        for index, color in queries:
            right = dp_right[color - 1][index]
            left = dp_left[color - 1][index]

            if left != -1 and right != -1:
                result_list.append(min(right, left))
            elif left == -1 and right != -1:
                result_list.append(right)
            elif left != -1 and right == -1:
                result_list.append(left)
            else:
                result_list.append(-1)

        return result_list



