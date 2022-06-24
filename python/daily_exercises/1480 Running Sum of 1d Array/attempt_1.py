from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)
        running_sum_list = []
        running_sum_list.append(nums[0])

        for index in range(1, len_nums):
            number = nums[index]
            running_sum = running_sum_list[index - 1] + number
            running_sum_list.append(running_sum)

        return running_sum_list



if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4]
    output = solution.runningSum(nums)
    print(output)