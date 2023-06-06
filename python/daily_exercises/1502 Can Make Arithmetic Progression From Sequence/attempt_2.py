class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        n = len(arr)
        min_num = float("inf")
        max_num = -float("inf")

        for num in arr:
            min_num = min(num, min_num)
            max_num = max(num, max_num)

        step_size = (max_num - min_num) / (n - 1)

        if (step_size % 1) != 0:
            return False
        else:
            step_size = int(step_size)

        if step_size == 0:
            return True

        step_set = set()

        for num in arr:
            if (num - min_num) % step_size != 0:
                return False
            else:
                step_set.add(num)

        return len(step_set) == n
