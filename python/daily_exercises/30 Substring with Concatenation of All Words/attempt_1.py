import copy
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if len(s) % 3 != 0:
            return []

        s_len = len(s) // 3
        w_len = len(words)
        one_w_len = len(words[0])

        dp = [[0] * w_len for _ in range(s_len)]

        index_dic = {}

        for index, word in enumerate(words):
            index_dic[word] = index

        pointer = 0

        for start_index in range(0, len(s) - one_w_len, one_w_len):
            cur_word = s[start_index:(start_index + one_w_len)]

            if cur_word in index_dic:
                word_pointer = index_dic[cur_word]
                dp[pointer][word_pointer] = 1
            pointer += 1

        res = []

        for start_index in range(0, s_len - w_len, 1):

            cur_section = dp[start_index:(start_index + w_len)]

            possible = True

            for index in range(w_len):
                sum = 0

                for section in cur_section:
                    sum += section[index]

                if sum != 1:
                    possible = False
                    break

            if possible:
                res.append(start_index*one_w_len)

        return res


