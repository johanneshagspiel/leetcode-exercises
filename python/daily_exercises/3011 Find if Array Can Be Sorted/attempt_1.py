from collections import defaultdict

class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_bit_dic = defaultdict(int)

        unique_numbers = list(set(nums))

        for bit in range(10):
            for i in range(len(unique_numbers)):
                num = unique_numbers[i]
                bit_count = set_bit_dic[num]

                if (num & (1 << bit)) != 0:
                    bit_count += 1

                set_bit_dic[num] = bit_count

        n = len(nums)

        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] <= nums[j + 1]:
                    continue
                else:
                    if set_bit_dic[nums[j]] == set_bit_dic[nums[j + 1]]:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    else:
                        return False

        return True
