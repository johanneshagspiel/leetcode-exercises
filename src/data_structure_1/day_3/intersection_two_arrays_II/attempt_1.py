import collections
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) > nums2:
            temp = nums2
            nums2 = nums1
            nums1 = temp
            
        dic_2 = {}
        for number in nums2:
            if number not in dic_2:
                dic_2[number] = [True]
            else:
                prev_result = dic_2[number]
                prev_result.append(True)
                dic_2[number] = prev_result

        intersection_list = []

        for number in nums1:
            if number in dic_2:
                prev_result = dic_2[number]
                prev_result.pop()
                intersection_list.append(number)

                if len(prev_result) == 0:
                    del dic_2[number]
                else:
                    dic_2[number] = prev_result

        return intersection_list


if __name__ == '__main__':
    solution = Solution()

    input_1 = [2,2,1]
    input_1_2 = [2]
    output_1 = solution.intersect(input_1, input_1_2)
    expected_output = [2,2]
    print(output_1)
