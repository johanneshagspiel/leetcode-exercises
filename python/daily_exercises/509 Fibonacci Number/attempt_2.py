class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0

        elif n == 1:
            return 1

        prev_2 = 0
        prev_1 = 1

        for num in range(n - 1):
            res = prev_2 + prev_1

            prev_2 = prev_1
            prev_1 = res

        return res
    