class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        num = x
        count = 1

        while count < n:
            bits = 0
            keep_going = True
            while keep_going:
                mask = (1 << bits)
                checkable = x & mask
                if checkable > 0:
                    bits += 1
                else:
                    rem = num & mask
                    num = num ^ mask
                    if rem != 0:
                        bits += 1
                    else:
                        keep_going = False
            count += 1

        return num
