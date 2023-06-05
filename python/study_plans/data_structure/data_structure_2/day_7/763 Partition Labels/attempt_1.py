from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        seen_dic = {}
        N = len(s)

        for index, letter in enumerate(s):

            if letter in seen_dic:
                prev = seen_dic[letter]
                seen_dic[letter] = (prev[0], index)
            else:
                seen_dic[letter] = (index, index)


        interval_list = list(seen_dic.values())

        int_start = interval_list[0][0]
        int_end = interval_list[0][1]

        res_list = []

        for cur_start, cur_end in interval_list[1:]:
            if cur_start > int_end:
                interval_length = int_end - int_start + 1
                res_list.append(interval_length)

                int_start = cur_start
                int_end = cur_end
            elif cur_end > int_end:
                int_end = cur_end

        interval_length = int_end - int_start + 1
        res_list.append(interval_length)

        return res_list


