class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        num = x
        n -= 1
        position = 0

        while n > 0:
            mask = 1 << position
            if x & mask == 0:
                num |= (1 & n) * mask
                n = n >> 1
            position += 1

        return num

