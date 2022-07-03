from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        def get_wiggle_sequence(mode, array, count, compare_number):
            if len(array) == 0:
                return count
            elif mode == 0:
                for index, number in enumerate(array):
                    if number > compare_number:
                        count += 1
                        return get_wiggle_sequence(1, array[(index+1):], count, number)
                return count

            elif mode == 1:
                for index, number in enumerate(array):
                    if number < compare_number:
                        count += 1
                        return get_wiggle_sequence(0, array[(index+1):], count, number)
                return count


        start_number = nums[0]
        rest_array = nums[1:]

        larger = get_wiggle_sequence(0, rest_array, 1, start_number)
        smaller = get_wiggle_sequence(1, rest_array, 1, start_number)

        if len(rest_array) > 1:
            skip_first = self.wiggleMaxLength(rest_array)
            return max(skip_first, larger, smaller)

        else:
            return max(larger, smaller)


