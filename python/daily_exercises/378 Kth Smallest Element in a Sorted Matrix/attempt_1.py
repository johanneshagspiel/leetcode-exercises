import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        priority_list = []

        n = len(matrix)
        largest_num = -float("inf")

        for i in range(n):
            for j in range(n):
                cur_num = matrix[i][j]

                if len(priority_list) == k:
                    if cur_num <= largest_num:
                        heapq.heappush(priority_list, cur_num)
                        priority_list[::] = priority_list[:-1]
                        largest_num = priority_list[-1]

                else:
                    heapq.heappush(priority_list, cur_num)
                    largest_num = max(largest_num, cur_num)

        return priority_list[-1]
