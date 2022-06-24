
def isBadVersion(version):
    return version >= 2

class Solution(object):

    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:

            pivot = left + ((right - left) // 2)
            pivot_boolean = isBadVersion(pivot)

            if pivot_boolean:
                right = pivot
            else:
                left = pivot + 1

        return left


if __name__ == '__main__':
    solution = Solution()

    input_1 = 3
    output_1 = solution.firstBadVersion(input_1)
    expected_1 = 2

    print(1)
    print(output_1)
    print(output_1 == expected_1)
    print(" ")
