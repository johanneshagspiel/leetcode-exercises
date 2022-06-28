from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        def rec(cards_left, card_list, acc_points):

            if cards_left == 0:
                return acc_points
            else:
                take_left = rec(cards_left - 1, card_list[1:], acc_points + card_list[0])
                take_right = rec(cards_left - 1, card_list[:-1], acc_points + card_list[-1])
                return max(take_left, take_right)

        return rec(k, cardPoints, 0)