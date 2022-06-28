from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        mem_dic = {}
        n = len(nums)

        def rec(i):

            if i < 0:
                return (0, 0)

            elif i in mem_dic:
                return mem_dic[i]

            else:

                sublist = [(0, 1)]

                for j in range(i - 1, -1, -1):
                    if nums[j] < nums[i]:
                        sublist.append(rec(j))

                longest = max(sublist)[0]
                count = sum([x[1] for x in sublist if x[0] == longest])

                mem_dic[i] = (longest + 1, count)

                return (longest + 1, count)

        subsequences = [rec(i) for i in range(n - 1, -1, -1)]
        max_subsequence_len = max(subsequences)[0]
        max_count = sum([x[1] for x in subsequences if x[0] == max_subsequence_len])

        return max_count