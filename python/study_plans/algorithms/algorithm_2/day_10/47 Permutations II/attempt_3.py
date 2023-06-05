import collections
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        results = []

        def back_track(cur_permutation, counter):

            if len(cur_permutation) == n:
                results.append(cur_permutation[::])
                return

            for number in counter:
                if counter[number] > 0:
                    cur_permutation.append(number)
                    counter[number] -= 1

                    back_track(cur_permutation, counter)

                    cur_permutation.pop()
                    counter[number] += 1

        counter = collections.Counter(nums)
        back_track([], counter)
        return results
