from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        left_pointer = 0
        right_pointer = 0
        result = 0
        combinations = []

        len_nums = len(nums) - 1

        while left_pointer < len_nums or right_pointer < len_nums:
            acc = 1
            section = nums[left_pointer:(right_pointer + 1)]
            product = [acc := acc * x for x in section][-1]

            if product < k:
                result += 1
                combinations.append(section)

                if right_pointer < len_nums:
                    right_pointer += 1
                else:
                    if left_pointer < len_nums:
                        left_pointer += 1
            else:
                if left_pointer != right_pointer:
                    left_pointer += 1
                else:
                    right_pointer += 1
        print(combinations)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarrayProductLessThanK([10,5,2,6], 100))
