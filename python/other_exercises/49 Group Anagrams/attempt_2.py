from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count_dic = defaultdict(list)

        for string in strs:

            count_array = [0 for _ in range(26)]

            for char in string:
                count_array[ord(char) - ord('a')] += 1

            key = "".join([str(x) + "#" for x in count_array])
            count_dic[key].append(string)

        res = []

        for el_list in count_dic.values():
            res.append(el_list)

        return res
