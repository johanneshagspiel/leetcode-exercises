class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winner_set = {x[0] for x in matches}
        loser_set = {x[1] for x in matches}

        only_winner_set = winner_set - loser_set
        only_winner_list = [x for x in only_winner_set]
        only_winner_list.sort()

        loser_counter = collections.Counter([x[1] for x in matches])
        one_loser_list = []

        for player, lost_count in loser_counter.items():
            if lost_count == 1:
                one_loser_list.append(player)
        one_loser_list.sort()

        res = []
        res.append(only_winner_list)
        res.append(one_loser_list)

        return res
