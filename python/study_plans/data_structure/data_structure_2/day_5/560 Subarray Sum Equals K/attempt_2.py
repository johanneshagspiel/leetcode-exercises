from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cur_sum = 0
        count = 0

        dic = {}
        dic[0] = 1

        for i in range(len(nums)):
            cur_sum += nums[i]

            remainder = cur_sum - k

            if remainder in dic:
                count += dic[remainder]

            new_entr = dic.get(cur_sum, 0) + 1
            dic[cur_sum] = new_entr

        return count

