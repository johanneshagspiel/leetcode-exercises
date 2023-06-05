from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        mem_dic = {}
        n = len(nums)

        def rec_mem(i):

            if i in mem_dic:
                return mem_dic[i]

            else:

                subsequences = [(0, 1)]

                for j in range(i - 1, -1, -1):
                    if nums[j] < nums[i]:
                        subsequences.append(rec_mem(j))

                longest_subsequences = max(subsequences)[0]
                count_subsequences_longest = sum([x[1] for x in subsequences if x[0] == longest_subsequences])

                mem_dic[i] = (longest_subsequences + 1, count_subsequences_longest)
                return (longest_subsequences + 1, count_subsequences_longest)

        subsequences = [rec_mem(i) for i in range(n -1, -1, -1)]
        max_len = max(subsequences)[0]
        max_count = sum([x[1] for x in subsequences if x[0] == max_len])
        return max_count
    