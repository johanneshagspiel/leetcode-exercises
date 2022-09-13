import collections
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        tokens.sort(reverse=False)
        queue = collections.deque(tokens)

        keep_going = True

        score = 0
        power = power

        while keep_going:

            pop_token = True

            while pop_token:

                if len(queue) > 0:

                    min_power = queue[0]

                    if power >= min_power:
                        score += 1
                        power -= queue.popleft()

                    else:
                        pop_token = False

                else:
                    keep_going = False
                    pop_token = False

            if len(queue) <= 2 or score == 0:
                keep_going = False
            else:
                power += queue.pop()
                score -= 1

        return score
