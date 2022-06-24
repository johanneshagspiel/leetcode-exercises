from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        results = 0
        combinations = []
        len_nums = len(nums)
        memo_dic = {}

        for start_index in range(len_nums):
            for end_index in range(start_index, len_nums, 1):

                previous_key = str(start_index) + "-" + str(end_index - 1)
                if previous_key in memo_dic:
                    previous_product = memo_dic[previous_key]
                    product = previous_product * nums[end_index]
                else:
                    acc = 1
                    section = nums[start_index:(end_index+1)]
                    product = [acc := acc * x for x in section][-1]

                key = str(start_index) + "-" + str(end_index)
                memo_dic[key] = product

                if product < k:
                    results += 1
                    combinations.append(section)
                else:
                    break

        return results

if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarrayProductLessThanK([10,5,2,6], 100))
