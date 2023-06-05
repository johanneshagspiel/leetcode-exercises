class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        else:

            other_half = 0

            while other_half < x:
                other_half = other_half * 10 + x % 10
                x = x // 10

            if (other_half == x) or (x == (other_half // 10)):
                return True
            else:
                return False
