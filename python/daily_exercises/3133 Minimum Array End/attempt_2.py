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
            num = (num + 1) | x
            count += 1

        return num
                    