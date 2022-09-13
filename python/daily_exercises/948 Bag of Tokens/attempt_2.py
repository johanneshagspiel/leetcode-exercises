import collections
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        keep_going = True
        tokens.sort(reverse=False)
        queue = collections.deque(tokens)

        power = power
        score = 0

        while keep_going:

            pop_tokens = True

            while pop_tokens:

                if len(queue) > 0:
                    min_power = queue[0]

                    if power >= min_power:
                        power -= queue.popleft()
                        score += 1
                    else:
                        pop_tokens = False

                else:
                    pop_tokens = False
                    keep_going = False

            if len(queue) <= 2 or score == 0:
                keep_going = False
            else:
                score -= 1
                power += queue.pop()

        return score


