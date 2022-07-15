from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        max_level = len(triangle)

        def rec_mem(level, index, mem_dic):

            if level == max_level:
                return triangle[level][index]

            elif (level, index) in mem_dic:
                return mem_dic[(level, index)]

            else:
                result = triangle[level][index] + min(rec_mem(level+1, index, mem_dic), rec_mem(level+1, index+1, mem_dic))
                mem_dic[(level, index)] = result
                return result

        return rec_mem(0, 0, {})
