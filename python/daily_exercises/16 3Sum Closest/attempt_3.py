import bisect


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        dif = float("inf")
        n = len(nums)
        nums.sort()

        for i in range(n):
            for j in range(i + 1, n):

                complement = target - nums[i] - nums[j]
                hi = bisect.bisect_right(nums, complement, j + 1)
                lo = hi - 1

                if hi < n and abs(complement - nums[hi]) < abs(dif):
                    dif = complement - nums[hi]

                if lo > j and abs(complement - nums[lo]) < abs(dif):
                    dif = complement - nums[lo]

            if dif == 0:
                return target

        return target - dif
