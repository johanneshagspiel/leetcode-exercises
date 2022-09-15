import collections
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        tokens.sort(reverse=False)
        queue = collections.deque(tokens)

        score = 0
        power = power

        keep_going = True

        while keep_going:

            pop_token = True

            while pop_token:

                if len(queue) > 0:

                    min_power = queue[0]

                    if min_power <= power:
                        score += 1
                        power -= queue.popleft()
                    else:
                        pop_token = False

                else:
                    keep_going = False
                    pop_token = False

            if score == 0 or len(queue) <= 2:
                keep_going = False
            else:
                power += queue.pop()
                score -= 1

        return score


