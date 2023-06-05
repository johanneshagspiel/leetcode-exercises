class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return Solution.search_with_start_index(nums, target, 0)

    @staticmethod
    def search_with_start_index(nums, target, start_index):

        mid_point_index = int(len(nums) / 2)
        mid_point_value = nums[mid_point_index]

        if len(nums) == 1:
            if mid_point_value == target:
                return start_index + mid_point_index
            else:
                return -1

        else:
            if mid_point_value == target:
                return start_index + mid_point_index

            elif mid_point_value > target:
                return Solution.search_with_start_index(nums[:mid_point_index], target, start_index)

            elif mid_point_value < target:
                return Solution.search_with_start_index(nums[mid_point_index:], target, start_index + mid_point_index)


if __name__ == '__main__':
    solution = Solution()

    input_1 = [-1,0,3,5,9,12]
    target_1 = 9
    output_1 = solution.search(input_1, target_1)
    expected_1 = 4

    print(1)
    print(output_1)
    print(output_1 == expected_1)
    print(" ")


    input_2 = [-1,0,3,5,9,12]
    target_2 = 2
    output_2 = solution.search(input_2, target_2)
    expected_2 = -1

    print(2)
    print(output_2)
    print(output_2 == expected_2)
    print(" ")

    input_3 = [-1,0,3,5,9,12]
    target_3 = 12
    output_3 = solution.search(input_3, target_3)
    expected_3 = 5

    print(3)
    print(output_3)
    print(output_3 == expected_3)
    print(" ")
