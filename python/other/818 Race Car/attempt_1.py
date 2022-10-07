import collections


class Solution:
    def racecar(self, target: int) -> int:

        queue = collections.deque()

        queue.append((0, 1, 0))
        visited = set()

        while queue:

            position, speed, moves = queue.popleft()

            if (position, speed) in visited:
                continue

            else:
                visited.add((position, speed))

                if position == target:
                    return moves

                else:
                    queue.append((position + speed, speed * 2, moves + 1))

                    if (position + speed > target and speed > 0) or (position + speed < target and speed < 0):
                        queue.append((position, -1 if speed > 0 else 1, moves + 1))
