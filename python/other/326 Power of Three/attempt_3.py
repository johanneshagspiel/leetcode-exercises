import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n <= 0:
            return False

        base  = math.log10(n) / math.log10(3)
        return (base % 1) == 0
