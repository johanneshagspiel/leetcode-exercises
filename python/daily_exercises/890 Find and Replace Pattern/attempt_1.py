import collections
import copy
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        pattern_char_dic = {}

        for char in pattern:
            pattern_char_dic[char] = True

        pattern_char_queue = collections.deque()

        for char in pattern_char_dic.keys():
            pattern_char_queue.append(char)

        result_list = []

        for word in words:
            cur_pattern = ""

            cur_pattern_char_deque = copy.deepcopy(pattern_char_queue)
            char_dic = {}

            for char in word:
                if char in char_dic:
                    pattern_letter = char_dic[char]
                else:
                    if len(cur_pattern_char_deque) == 0:
                        break
                    else:
                        pattern_letter = cur_pattern_char_deque.popleft()
                        char_dic[char] = pattern_letter
                cur_pattern += pattern_letter

            if cur_pattern == pattern:
                result_list.append(word)

        return result_list
