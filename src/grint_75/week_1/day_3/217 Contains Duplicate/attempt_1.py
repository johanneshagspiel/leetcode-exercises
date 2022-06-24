from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_counter = Counter(nums)
        max_count = number_counter.most_common(n=1)[0][1]

        return max_count == 1

