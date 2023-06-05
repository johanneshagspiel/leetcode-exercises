from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        N = len(nums)

        count = 0
        sum = 0

        dic = {}
        dic[0] = 1

        for i in range(N):
            sum += nums[i]
            rest = sum - k

            if rest in dic:
                count += dic[rest]

            new_ent = dic.get(sum, 0) + 1
            dic[sum] = new_ent

        return count
