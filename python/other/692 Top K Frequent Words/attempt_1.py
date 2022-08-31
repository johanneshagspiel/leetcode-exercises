import collections
import random
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        frequency_counter_dic = collections.Counter(words)




