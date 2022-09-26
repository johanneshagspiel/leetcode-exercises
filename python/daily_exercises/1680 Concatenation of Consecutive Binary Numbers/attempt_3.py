class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        prev_len = 0

        for num in range(1, n + 1):
            if num & (num - 1) == 0:
                prev_len += 1

            res = ((res << prev_len) | num) % (pow(10, 9) + 7)

        return res
