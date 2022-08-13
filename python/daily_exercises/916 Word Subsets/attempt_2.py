import collections
import copy
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        max_word_count = [0] * 26

        for word2 in words2:
            word2_count = [0] * 26

            for char in word2:
                word2_count[ord(char) - ord('a')] += 1

            for index, value in enumerate(word2_count):
                max_word_count[index] = max(max_word_count[index], value)

        res = []

        for word1 in words1:
            word_1_counter = [0] * 26
            for char in word1:
                word_1_counter[ord(char) - ord('a')] += 1

            all_larger = True
            for index, value in enumerate(word_1_counter):
                if value < max_word_count[index]:
                    all_larger = False
                    break

            if all_larger:
                res.append(word1)

        return res
