import collections
import math


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        n_count = collections.Counter(str(n))

        max_digit = math.ceil(math.log10(10**9) / math.log10(2)) + 1

        for iteration in range(max_digit):
            new_val = 1 << iteration
            new_val_count = collections.Counter(str(new_val))

            if n_count == new_val_count:
                return True

        return False
