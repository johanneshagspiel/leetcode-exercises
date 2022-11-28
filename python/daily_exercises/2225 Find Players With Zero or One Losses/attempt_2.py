class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        lost_count = {}

        for winner, loser in matches:

            if loser not in lost_count:
                lost_count[loser] = 1
            else:
                prev_los = lost_count[loser]

                if prev_los == -1:
                    lost_count[loser] = 1
                else:
                    lost_count[loser] += 1

            if winner not in lost_count:
                lost_count[winner] = -1

        no_loss = []
        one_loss = []

        for loser, count in lost_count.items():

            if count == -1:
                no_loss.append(loser)

            elif count == 1:
                one_loss.append(loser)

        return [sorted(no_loss), sorted(one_loss)]
