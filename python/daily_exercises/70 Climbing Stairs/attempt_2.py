class Solution:
    def climbStairs(self, n: int) -> int:
        two_steps = 1
        one_step = 1

        for i in range(n - 2, -1, -1):
            current = one_step + two_steps

            two_steps = one_step
            one_step = current

        return one_step