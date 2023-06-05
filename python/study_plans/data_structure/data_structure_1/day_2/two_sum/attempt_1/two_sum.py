from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        number_dic = {}

        for index_first_number, first_number in enumerate(nums):
            second_number = target - first_number

            if second_number in number_dic:
                index_second_number = number_dic[second_number]

                return [index_first_number, index_second_number]

            else:
                number_dic[first_number] = index_first_number


if __name__ == '__main__':
    solution = Solution()

    input_1 = [2,7,11,15]
    target_1 = 9
    output_1 = solution.twoSum(input_1, target_1)
    expected_1 = 8

    print(output_1)