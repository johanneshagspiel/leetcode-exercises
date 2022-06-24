from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        moves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

        explore_positions_queue = deque([(0, 0)])
        visited = set()
        steps = 0

        while explore_positions_queue:

            current_queue_length = len(explore_positions_queue)

            for i in range(current_queue_length):
                current_x, current_y = explore_positions_queue.popleft()

                if current_x == x and current_y == y:
                    return steps

                for x_move, y_move in moves:
                    new_x = current_x + x_move
                    new_y = current_y + y_move

                    if (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        explore_positions_queue.append((new_x, new_y))

            steps += 1


if __name__ == '__main__':
    solution = Solution()
    x = 5
    y = 5
    output = solution.minKnightMoves(x, y)
    print(output)