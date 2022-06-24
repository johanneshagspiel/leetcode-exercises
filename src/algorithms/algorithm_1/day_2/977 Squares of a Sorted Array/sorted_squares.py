import collections
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        deque_nums = collections.deque(nums)
        result_list = []

        first_entry = pow(deque_nums.popleft(), 2)
        last_entry = pow(deque_nums.pop(), 2)

        right_side_not_done, left_side_not_done = True, True

        while right_side_not_done or left_side_not_done:

            if right_side_not_done and not left_side_not_done:
                result_list.append(last_entry)

                if len(deque_nums) > 0:
                    last_entry = pow(deque_nums.pop(), 2)
                else:
                    right_side_not_done = False

            elif left_side_not_done and not right_side_not_done:
                result_list.append(first_entry)

                if len(deque_nums) > 0:
                    first_entry = pow(deque_nums.popleft(), 2)
                else:
                    left_side_not_done = False

            else:
                if last_entry > first_entry:
                    result_list.append(last_entry)

                    if len(deque_nums) > 0:
                        last_entry = pow(deque_nums.pop(), 2)
                    else:
                        right_side_not_done = False
                else:
                    result_list.append(first_entry)

                    if len(deque_nums) > 0:
                        first_entry = pow(deque_nums.popleft(), 2)
                    else:
                        left_side_not_done = False

        return result_list[::-1]

if __name__ == '__main__':
    solution = Solution()

    input_1 = [-4,-1,0,3,10]
    output_1 = solution.sortedSquares(nums=input_1)
    print(output_1)
    expected_1 = [0,1,9,16,100]

