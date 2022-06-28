from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        max_len = 1
        entry_dic = {}
        result_list = []

        for num in nums:
            n = len(result_list)
            
            key = str(num) + "_1"
            if key not in entry_dic:
                entry_dic[key] = True
                result_list.append((num, 1))

            for compare_num, counts in result_list[:n+1]:

                if compare_num < num:
                    new_key = str(num) + "_" + str(counts + 1)
                    if new_key not in entry_dic:
                        entry_dic[new_key] = True
                        result_list.append((num, counts + 1))

                        if counts + 1 > max_len:
                            max_len = counts + 1

        return max_len
