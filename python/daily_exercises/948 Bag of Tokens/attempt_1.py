import collections
import heapq
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        score = 0
        power = power
        keep_going = True

        tokens.sort(reverse=False)
        queue = collections.deque(tokens)

        while keep_going:

            pop_token = True

            while pop_token:

                if len(queue) > 0:
                    min_power = queue[0]

                    if min_power > power:
                        pop_token = False
                    else:
                        power -= queue.popleft()
                        score += 1
                else:
                    pop_token = False
                    keep_going = False


            if len(queue) <= 1 or score == 0:
                keep_going = False
            else:
                power += queue.pop()
                score -= 1

        return score
