class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        else:
            string_list = list(bin(abs(n))[2:])
            number_of_ones = sum(list(map(lambda x: int(x), string_list)))
            return 1 == number_of_ones


if __name__ == "__main__":
    solution = Solution()
    solution.isPowerOfTwo(16)
