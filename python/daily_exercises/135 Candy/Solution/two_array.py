from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        left_to_right = [1 for _ in range(n)]
        right_to_left = [1 for _ in range(n)]

        for index in range(1, n):
            if ratings[index] > ratings[index-1]:
                left_to_right[index] = left_to_right[index-1] + 1

        for index in range(n-2, -1, -1):
            if ratings[index] > ratings[index+1]:
                right_to_left[index] = right_to_left[index+1] + 1

        sum = 0
        for index in range(n):
            sum += max(left_to_right[index], right_to_left[index])
        return sum