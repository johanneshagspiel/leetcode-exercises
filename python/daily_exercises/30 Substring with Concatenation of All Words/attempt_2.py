import collections
import copy
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        word_counter = collections.Counter(words)

        one_word_len = len(words[0])
        words_len = len(words)
        s_list = len(s)
        substring_len = words_len * one_word_len

        def check(start):
            remaining = copy.deepcopy(word_counter)

            for start_index in range(start, start + substring_len, one_word_len):
                cur_word = s[start_index:(start_index+one_word_len)]

                if cur_word in remaining:
                    if remaining[cur_word] == 0:
                        return False
                    else:
                        remaining[cur_word] -= 1
                else:
                    return False

            return True


        res = []

        for start_index in range(s_list - substring_len + 1):
            include = check(start_index)
            if include:
                res.append(start_index)

        return res
