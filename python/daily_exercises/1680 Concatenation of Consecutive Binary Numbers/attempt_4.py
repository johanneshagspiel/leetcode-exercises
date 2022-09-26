class Solution:
    def concatenatedBinary(self, n: int) -> int:

        acc = 0
        prev_len = 0

        for num in range(1, n+1):

            if num & (num - 1) == 0:
                prev_len += 1

            acc = acc << prev_len
            acc = acc | num
            acc = acc % (pow(10 ,9) + 7)

        return acc

