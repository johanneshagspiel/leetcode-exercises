from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        def rec(cards_left, points_accumulated, card_list, mem_dic):

            if cards_left < 0:
                return points_accumulated

            elif cards_left in mem_dic:
                return mem_dic[cards_left]

            else:
                take_left = rec(cards_left - 1, points_accumulated + card_list[0], card_list[1:], mem_dic)
                take_right = rec(cards_left - 1, points_accumulated + card_list[-1], card_list[:-1], mem_dic)
                mem_dic[cards_left] = points_accumulated + max(take_left, take_right)
                return mem_dic[cards_left]

        return rec(k, 0, cardPoints, {})
