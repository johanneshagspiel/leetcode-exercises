class Solution:
    def minPartitions(self, n: str) -> int:

        num_list = [int(x) for x in list(n)]

        return max(num_list)