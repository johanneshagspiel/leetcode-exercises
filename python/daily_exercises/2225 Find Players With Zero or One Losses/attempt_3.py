class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        count_array = [0]*100001

        for winner, loser in matches:

            if count_array[winner] == 0:
                count_array[winner] = -1

            if count_array[loser] == -1:
                count_array[loser] = 1
            else:
                count_array[loser] += 1

        no_loss = []
        one_loss = []

        for num, count in enumerate(count_array):
            if count == -1:
                no_loss.append(num)

            if count == 1:
                one_loss.append(num)

        return [no_loss, one_loss]