
class Solution:
    def concatenatedBinary(self, n: int) -> int:

        acc = 0
        length = 0

        for num in range(1, n+1):

            if (num & (num - 1)) == 0:
                length += 1

            acc = acc << length
            acc = (acc | num) % (pow(10, 9) + 7)

        return acc
