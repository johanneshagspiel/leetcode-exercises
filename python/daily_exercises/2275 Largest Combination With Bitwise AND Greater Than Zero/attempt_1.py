class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        max_count = 0

        for bit in range(24):
            current_count = 0
            for candidate in candidates:
                if (candidate & (1 << bit)) != 0:
                    current_count += 1
            max_count = max(max_count, current_count)

        return max_count
