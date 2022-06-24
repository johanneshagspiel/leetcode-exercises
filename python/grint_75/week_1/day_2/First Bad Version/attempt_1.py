# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left_position = 1
        right_position = n

        while left_position < right_position:

            pivot_value = left_position + ((right_position - left_position) // 2)
            pivot_boolean = isBadVersion(pivot_value)

            if pivot_boolean:
                right_position = pivot_value
            else:
                left_position = pivot_value + 1

        return left_position

