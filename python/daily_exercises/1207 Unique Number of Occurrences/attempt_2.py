import collections


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        frequency_counter = collections.Counter(arr)
        frequency_set = set()

        for counter in frequency_counter.values():
            if counter in frequency_set:
                return False
            frequency_set.add(counter)

        return True