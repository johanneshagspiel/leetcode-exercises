class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()

        first_num = arr[0]
        prev_num = arr[1]

        compare_diff = prev_num - first_num

        for num in arr[2:]:
            cur_dif = num - prev_num

            if cur_dif != compare_diff:
                return False
            else:
                prev_num = num

        return True
