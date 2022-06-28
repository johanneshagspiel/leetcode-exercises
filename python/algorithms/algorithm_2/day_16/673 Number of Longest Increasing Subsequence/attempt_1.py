import copy
import json
from bisect import bisect_left
from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        sub_start = [nums[0]]
        result_list = []
        result_list.append(sub_start)

        for num in nums[1:]:

            n = len(result_list)
            for sub in result_list[:n]:
                if sub[-1] < num:
                    sub.append(num)
                else:
                    temp = copy.deepcopy(sub)
                    i = bisect_left(temp, num)
                    temp[i] = num
                    result_list.append(temp)

        len_list = [len(x) for x in result_list]
        max_len = max(len_list)
        count = 0

        for len_it in len_list:
            if len_it == max_len:
                count += 1

        return count
