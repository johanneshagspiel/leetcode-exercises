from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_dic = {}

        for string in strs:

            st_list = [*string]
            st_list.sort()

            sorted_str = "".join(st_list)

            if sorted_str not in sorted_dic:
                sorted_dic[sorted_str] = []
            sorted_dic[sorted_str].append(string)

        res = []

        for list in sorted_dic.values():
            res.append(list)

        return res
