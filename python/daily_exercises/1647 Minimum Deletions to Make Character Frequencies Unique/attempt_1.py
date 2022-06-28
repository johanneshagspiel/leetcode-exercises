import collections
class Solution:
    def minDeletions(self, s: str) -> int:

        char_counter = collections.Counter(s)
        deletions = 0
        amount_counter = {}

        for char, amount in char_counter.items():
            while amount in amount_counter:
                deletions += 1
                amount -= 1
            if amount > 0:
                amount_counter[amount] = char

        return deletions
