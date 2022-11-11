class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        prev_num = -float("inf")
        for i in range(len(nums)):
            cur_num = nums[i]

            if cur_num == prev_num:
                nums[i] = '#'
            else:
                prev_num = cur_num

        slow = 1
        fast = 1
        found = False
        while fast < len(nums) and slow < len(nums):
            if not found:
                if nums[slow] == '#':
                    found = True
                else:
                    slow += 1
            else:
                if nums[fast] == '#':
                    fast += 1
                else:
                    if fast > slow:
                        nums[slow], nums[fast] = nums[fast], nums[slow]
                        found = False
                    else:
                        fast += 1

        return slow
