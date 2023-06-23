import collections


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        left_to_right = [0 for _ in range(n)]
        for i, num in enumerate(nums):

            left_to_right[i] = num

            if i - 1 >= 0 :

                left_to_right[i] += left_to_right[i - 1]

                j = i - k - 1

                if j >= 0:
                    left_to_right[i] -= nums[j]


        right_to_left = [0 for _ in range(n)]
        for i in range(n -1, -1, -1):
            num = nums[i]

            right_to_left[i] = num
            if (i + 1) <= (n - 1):
                right_to_left[i] += right_to_left[i + 1]

                j = i + k + 1

                if j <= (n - 1):
                    right_to_left[i] -= nums[j]

        result = []

        for i in range(n):

            if (i - k) >= 0 and (i + k) <= (n - 1):
                sum = right_to_left[i] + left_to_right[i] - nums[i]
                avg = sum  // ((2 * k) + 1)
                result.append(avg)
            else:
                result.append(-1)

        return result
