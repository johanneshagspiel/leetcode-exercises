class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        mem_dic = {}
        n = len(nums)
        res = 0

        for i in range(n - 2, -1, -1):
            cur_num = nums[i]

            for j in range(i + 1, n):
                other_num = nums[j]

                dif = other_num - cur_num
                add = 1

                if j in mem_dic:
                    if dif in mem_dic[j]:
                        add = mem_dic[j][dif]
                res = max(res, add + 1)

                if i not in mem_dic:
                    mem_dic[i] = {}
                if dif in mem_dic[i]:
                    prev_entry = mem_dic[i][dif]
                    mem_dic[i][dif] = max(prev_entry, add + 1)
                else:
                    mem_dic[i][dif] = add + 1

        return res
