from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        mem_dic = {}
        n = len(nums)

        def rec_mem(i):

            if i < 0:
                return (0, 0)

            elif i in mem_dic:
                return mem_dic[i]

            else:

                sub_sequences = [(0, 1)]

                for j in range(i-1, -1, -1):
                    if nums[j] < nums[i]:
                        sub_sequences.append(rec_mem(j))

                max_sequence_len = max(sub_sequences)[0]
                count_max_sequence = sum([x[1] for x in sub_sequences if x[0] == max_sequence_len])

                mem_dic[i] = (max_sequence_len + 1, count_max_sequence)
                return (max_sequence_len + 1, count_max_sequence)

        subsequences = [rec_mem(i) for i in range(n-1, -1, -1)]
        max_len = max(subsequences)[0]
        max_count = sum([x[1] for x in subsequences if x[0] == max_len])
        return max_count