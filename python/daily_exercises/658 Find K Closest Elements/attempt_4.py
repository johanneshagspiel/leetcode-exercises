class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        start_index = bisect_left(arr, x)

        left = start_index - 1
        right = start_index

        while (right - left - 1) < k:

            if left == -1:
                right += 1

            elif right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]
