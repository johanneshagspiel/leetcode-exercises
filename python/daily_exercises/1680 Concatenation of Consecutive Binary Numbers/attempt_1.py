class Solution:
    def concatenatedBinary(self, n: int) -> int:

        acc = ""

        for num in range(1, n+1):
            addition = bin(num)[2:]
            acc += addition

        res =  int(acc, 2)
        return res % (pow(10, 9) + 7)
