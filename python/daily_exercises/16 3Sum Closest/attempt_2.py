class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        n = len(nums)

        res = float("inf")
        min_dif = float("inf")

        for i in range(n):
            first_number = nums[i]

            left = i + 1
            right = n - 1

            while left < right:
                second_number = nums[left]
                third_number = nums[right]

                dif = target - first_number - second_number - third_number

                if abs(dif) < abs(min_dif):
                    min_dif = dif
                    res = first_number + second_number + third_number

                if dif == 0:
                   return target

                elif dif < 0:
                    right -= 1

                else:
                    left += 1

        return res
