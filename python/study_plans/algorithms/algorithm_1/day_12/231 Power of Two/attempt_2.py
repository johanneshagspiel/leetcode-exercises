class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        string_list = list(bin(abs(n))[2:])
        number_shifts = len(string_list)
        second_number = 1 << number_shifts
        result = n & second_number
        return result == n


if __name__ == "__main__":
    solution = Solution()
    solution.isPowerOfTwo(16)
