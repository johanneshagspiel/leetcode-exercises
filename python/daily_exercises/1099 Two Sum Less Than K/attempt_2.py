class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        low = 0
        high = 1000

        count = [0] * 1001

        result = -1

        for num in nums:
            count[num] += 1

        while low <= high:

            if low + high >= k or count[high] == 0:
                high -= 1

            else:
                if count[low] > (0 if low < high else 1):
                    result = max(result, low + high)

                low += 1

        return result