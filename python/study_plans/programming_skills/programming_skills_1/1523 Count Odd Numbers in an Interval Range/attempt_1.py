class Solution:
    def countOdds(self, low: int, high: int) -> int:

        nums_between = high - low - 1

        even_between = nums_between // 2

        low_odd = low % 2 == 1
        high_odd = high % 2 == 1

        if low_odd and high_odd:
            return even_between + 2

        else:
            return even_between + 1
