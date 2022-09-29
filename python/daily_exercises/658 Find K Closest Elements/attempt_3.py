from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        left = 0
        right = len(arr)

        while left < right:

            mid = left + ((right - left) // 2)

            if abs(arr[mid + k] - x) < abs(arr[mid] - x):
                right = mid

            else:
                left = mid - 1

        return arr[left:right+k]
        