class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)

        def rec(index, mem_dic):
            if index == (N - 1):
                return nums[-1]
            elif index > (N - 1):
                return 0
            elif index in mem_dic:
                return mem_dic[index]

            else:
                skip_one = rec(index + 1, mem_dic)
                take_this = nums[index] + rec(index + 2, mem_dic)
                res = max(skip_one, take_this)
                mem_dic[index] = res
                return res

        return rec(0, {})
