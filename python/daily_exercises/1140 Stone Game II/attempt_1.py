class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        def recMem(player, M, position, recDic):

            if position >= len(piles):
                return 0
            else:
                if (player, M, position) in recDic:
                    return recDic[(player, M, position)]
                else:

                    s = 0
                    res = -float("inf") if player else float("inf")

                    for X in range(1, min(2 * M, len(piles) - position) + 1):
                        newM = max(M, X)

                        s += piles[position + X - 1]

                        if player:
                            res = max(res, s + recMem(not player, newM, position + X, recDic))
                        else:
                            res = min(res, recMem(not player, newM, position + X, recDic))

                    recDic[(player, M, position)] = res

                    return recDic[(player, M, position)]

        return recMem(True, 1, 0, {})
