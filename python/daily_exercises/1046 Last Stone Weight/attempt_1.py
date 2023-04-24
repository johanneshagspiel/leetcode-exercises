import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [(-1)*stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            heavy_y = heapq.heappop(stones)
            heavy_x = heapq.heappop(stones)

            if heavy_x != heavy_y:
                new_stone = heavy_y - heavy_x
                heapq.heappush(stones, new_stone)

        if len(stones) == 1:
            return (-1) * stones.pop()
        else:
            return 0
