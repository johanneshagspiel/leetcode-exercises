class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """

        max_num = (2 ** maximumBit) - 1
        res = []
        previous_xor = 0

        for num in nums:
            new_xor = previous_xor ^ num
            new_res = max_num ^ new_xor

            res.append(new_res)
            previous_xor = new_xor

        return res[::-1]
