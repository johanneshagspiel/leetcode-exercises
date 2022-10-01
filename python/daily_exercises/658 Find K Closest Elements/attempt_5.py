class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        closest_index = bisect.bisect_left(arr, x)

        left = closest_index - 1
        right = closest_index

        while (right - left - 1) < k:

            if left == -1:
                right += 1

            elif right == len(arr) or abs(x - arr[left]) <= abs(x - arr[right]):
                left -= 1
            else:
                right += 1

        return arr[(left + 1):right]
