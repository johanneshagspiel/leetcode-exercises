from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        N = len(matchsticks)

        def rec(side_1, side_2, side_3, side_4, match_index, mem_dic):

            if side_1 == side_2 and side_1 == side_3 and side_1 == side_4 and side_2 == side_3 and side_2 == side_4 and \
                    side_3 == side_4 and match_index == N-1:
                return True

            elif match_index >= N-1:
                return False

            elif (side_1, side_2, side_3, side_4) in mem_dic:
                return mem_dic[(side_1, side_2, side_3, side_4, match_index)]

            else:

                match = matchsticks[match_index]

                side_1_res = rec(side_1+match, side_2, side_3, side_4, match_index+1, mem_dic)
                side_2_res = rec(side_1, side_2+match, side_3, side_4, match_index+1, mem_dic)
                side_3_res = rec(side_1, side_2, side_3+match, side_4, match_index+1, mem_dic)
                side_4_res = rec(side_1, side_2, side_3, side_4+match, match_index+1, mem_dic)

                result = any([side_1_res, side_2_res, side_3_res, side_4_res])
                mem_dic[(side_1, side_2, side_3, side_4, match_index)] = result
                return result

        return rec(0, 0, 0, 0, 0, {})
