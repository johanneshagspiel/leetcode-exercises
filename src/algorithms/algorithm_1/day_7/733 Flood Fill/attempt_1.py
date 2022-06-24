import collections
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        max_rows = len(image)
        max_columns = len(image[0])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        to_change_color = image[sr][sc]

        queue = collections.deque([(sr, sc)])
        visited = set()
        visited.add((sr, sc))

        while queue:
            current_row, current_column = queue.popleft()

            image[current_row][current_column] = newColor


            for row_move, column_move in directions:
                new_row = current_row + row_move
                new_column = current_column + column_move

                if new_row >= 0 and new_row < max_rows and new_column >= 0 and new_column < max_columns:
                    if (new_row, new_column) not in visited:
                        if image[new_row][new_column] == to_change_color:
                            visited.add((new_row, new_column))
                            queue.append((new_row, new_column))

        return image

if __name__ == "__main__":
    solution = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    output = solution.floodFill(image, sr, sc, newColor)
    print(output)