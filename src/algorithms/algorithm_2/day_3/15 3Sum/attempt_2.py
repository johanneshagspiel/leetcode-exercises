from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result_dic = {}

        nums.sort()
        n = len(nums)

        for first_number in range(n):
            first_value = nums[first_number]
            target = 0 - first_value

            left_pointer = first_number + 1
            right_pointer = n - 1

            while left_pointer < right_pointer:
                left_value = nums[left_pointer]
                right_value = nums[right_pointer]
                combined_value = left_value + right_value

                if combined_value == target:
                    result_dic[(first_value, left_value, right_value)] = True
                    left_pointer += 1
                elif combined_value < target:
                    left_pointer += 1
                else:
                    right_pointer -= 1

        return list(result_dic.keys())


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))