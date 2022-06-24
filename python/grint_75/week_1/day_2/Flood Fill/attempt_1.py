from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        max_x = len(image)
        max_y = len(image[0])

        stack = []
        start_point_color = image[sr][sc]
        stack.append((sr, sc))
        seen_location_dic = {}

        while len(stack) > 0:
            current_position = stack.pop()
            current_x = current_position[0]
            current_y = current_position[1]
            seen_location_dic[current_position] = True

            image[current_x][current_y] = newColor

            move_list = [(current_x + 1, current_y), (current_x - 1, current_y), (current_x, current_y + 1), (current_x, current_y - 1)]

            for move_x, move_y in move_list:
                if (move_x >= 0) and (move_x < max_x) and (move_y >= 0) and (move_y < max_y):
                    color_move = image[move_x][move_y]
                    if color_move == start_point_color:
                        if (move_x, move_y) not in seen_location_dic:
                            stack.append((move_x, move_y))

        return image





if __name__ == '__main__':
    solution = Solution()

    image = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    newColor = 1
    output_1 = solution.floodFill(image, sr, sc, newColor)
    expected_output = [[2,2,2],[2,2,2]]
    print(output_1)
