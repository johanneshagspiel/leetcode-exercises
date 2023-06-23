class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        seen_set = set()
        n = len(nums)
        max_res = 2

        for i in range(n - 1, -1, -1):
            cur_num = nums[i]

            for j in range(i - 1, -1, -1):

                other_num = nums[j]

                dif = cur_num - other_num

                if dif not in seen_set:
                    seen_set.add(dif)

                    res = 2

                    prev_num = other_num
                    for k in range(j - 1, -1, -1):
                        third_num = nums[k]
                        other_dif = prev_num - third_num

                        if other_dif == dif:
                            res += 1
                            prev_num = third_num

                    max_res = max(res, max_res)

        return max_res
