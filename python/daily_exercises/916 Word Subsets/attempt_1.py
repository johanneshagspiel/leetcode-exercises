import collections
import copy
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        result_list = []

        for word_1 in words1:

            universal_subset = True

            word_1_counter = collections.Counter(word_1)

            for word_2 in words2:

                cur_word_1_counter = copy.deepcopy(word_1_counter)

                for char in word_2:

                    if char not in cur_word_1_counter or cur_word_1_counter[char] == 0:
                        universal_subset = False
                        break
                    else:
                        cur_word_1_counter[char] -= 1

                if not universal_subset:
                    break

            if universal_subset:
                result_list.append(word_1)

        return result_list
