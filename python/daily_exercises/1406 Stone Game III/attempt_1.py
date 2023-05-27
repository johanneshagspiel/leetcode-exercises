class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)

        def recMem(player, position, memDic):

            if position >= n:
                return 0

            elif (player, position) in memDic:
                return memDic[(player, position)]

            else:

                res = -float("inf") if player else float("inf")
                s = 0

                for i in range(1, min(3, n - position) + 1):
                    s += stoneValue[position + i - 1]

                    if player:
                        res = max(res, s + recMem(not player, position + i, memDic))
                    else:
                        res = min(res, recMem(not player, position + i, memDic))

                memDic[(player, position)] = res
                return res

        maxAmount = sum(stoneValue)
        aliceMaxValue = recMem(True, 0, {})
        bobMaxValue = maxAmount - aliceMaxValue

        if aliceMaxValue > bobMaxValue:
            return "Alice"
        elif bobMaxValue > aliceMaxValue:
            return "Bob"
        else:
            return "Tie"
