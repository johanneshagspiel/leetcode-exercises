class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
        def recMem(player, position, M, memDic):

            if position >= n:
                return 0

            elif (player, position, M) in memDic:
                return memDic[(player, position, M)]

            else:

                res = -float("inf") if player else float("inf")
                s = 0

                for X in range(1, min(2 * M, n - position) + 1):

                    s += piles[position + X - 1]
                    newM = max(X, M)

                    if player:
                        res = max(res, s + recMem(not player, position + X, newM, memDic))
                    else:
                        res = min(res, recMem(not player, position + X, newM, memDic))

                memDic[(player, position, M)] = res
                return res

        return recMem(True, 0, 1, {})
