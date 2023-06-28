import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        n = len(costs)
        start_right_index = n - candidates
        end_left_index = candidates - 1

        if start_right_index <= end_left_index:
            end_left_index = n - 1
            start_right_index = n

        heap = []

        for index in range(end_left_index + 1):
            heap.append((costs[index], index))

        for index in range(start_right_index, n, 1):
            heap.append((costs[index], index))

        heapq.heapify(heap)

        result = 0
        crossed = end_left_index == (n - 1)

        for candidate in range(k):
            lowest_cost, index = heapq.heappop(heap)
            result += lowest_cost

            if not crossed:
                if index <= end_left_index:
                    end_left_index += 1
                    heapq.heappush(heap, (costs[end_left_index], end_left_index))

                elif index >= start_right_index:
                    start_right_index -= 1
                    heapq.heappush(heap, (costs[start_right_index], start_right_index))

                if start_right_index == (end_left_index + 1):
                    crossed = True

        return result
