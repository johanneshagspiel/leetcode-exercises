class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        count_array = [0 for _ in range(pow(10, 5) + 1)]
        min_num = float("inf")

        for num in nums:
            if num > 0:
                if num < pow(10, 5):
                    count_array[num - 1] += 1
                min_num = min(min_num, num)

        if min_num >= 2:
            return 1
        else:
            missing = -1

            for index, count in enumerate(count_array):
                if count == 0:
                    missing = index + 1
                    break

            if missing != -1:
                return missing
            else:
                return pow(10, 5) + 1
