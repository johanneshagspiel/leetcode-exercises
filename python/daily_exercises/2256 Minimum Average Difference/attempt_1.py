class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        res = []

        currentSum = 0
        currentCount = 1

        for i in range(len(nums)):
            currentSum += nums[i]
            currentAvg = int(currentSum / currentCount)
            res.append(currentAvg)
            currentCount += 1

        currentSum = 0
        currentCount = 1

        for i in range(len(nums) - 2, -1, -1):
            currentSum += nums[i + 1]
            currentAvg = int(currentSum / currentCount)
            prevAvg = res[i]
            absDif = abs(prevAvg - currentAvg)
            res[i] = absDif
            currentCount += 1

        min_ind = -1
        min_val = float("inf")

        for i, val in enumerate(res):
            if val < min_val:
                min_val = val
                min_ind = i

        return min_ind