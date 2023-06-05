from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dic = {}
        max_count = 0
        max_num = None

        for num in nums:
            if num in dic:
                prev_entry = dic[num]
                new_entry = prev_entry + 1
            else:
                new_entry = 1

            dic[num] = new_entry

            if new_entry > max_count:
                max_count = new_entry
                max_num = num

        return max_num

