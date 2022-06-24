from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result_dic = {}
        number_index_dic = {}
        n = len(nums)

        for index, number in enumerate(nums):
            number_index_dic[number] = index

        for first_index in range(n):
            first_number = nums[first_index]
            for second_index in range(first_index, n):
                    second_number = nums[second_index]
                    if first_number != second_number:
                        missing_value = 0 - first_number - second_number
                        if first_number != missing_value and second_number != missing_value:
                            if missing_value in number_index_dic:
                                result_list = [first_number, second_number, missing_value]
                                lowest_value = min(first_number, second_number, missing_value)
                                result_list.remove(lowest_value)
                                second_lowest_value = min(result_list)
                                result_list.remove(second_lowest_value)
                                third_lowest_value = result_list.pop()
                                key = str(lowest_value) + "-" + str(second_lowest_value) + "-" + str(third_lowest_value)
                                if key not in result_dic:
                                    result_dic[key] = [lowest_value, second_lowest_value, third_lowest_value]

        return list(result_dic.values())

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))