class Solution:
    def climbStairs(self, n: int) -> int:
        steps_arr = [0] * (n + 1)
        steps_arr[n] = 1
        steps_arr[n - 1] = 1

        for i in range(n - 2, -1, -1):
            steps_arr[i] = steps_arr[i + 1] + steps_arr[i + 2]

        return steps_arr[0]