from typing import List
from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if k == x:
            return arr

        closest_index = bisect_left(arr, x)

        left = closest_index - 1
        right = closest_index

        n = len(arr)

        while (right - left) > k:

            if left == 0:
                right += 1
                continue

            if right == (n - 1) or abs(arr[right] - x) >= abs(arr[left] - x):
                left -= 1
            else:
                right += 1

        return arr[(left+1):right]
