class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        else:

            divisor = 10
            split_list = []
            temp = x
            decimals = 1

            while divisor <= (10 * temp):
                remainder = temp % divisor
                temp -= remainder

                remainder /= 10 * decimals
                split_list.append(remainder)
                divisor *= 10
                decimals *= 10

            left = 0
            right = len(split_list) - 1

            while left <= right:

                left_val = split_list[left]
                right_val = split_list[right]

                if left_val != right_val:
                    return False
                else:
                    left += 1
                    right -= 1

            return True

