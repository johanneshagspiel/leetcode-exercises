from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        substring_count = 0
        N = len(s)

        for word in words:
            word_len = len(word)

            if word_len > N:
                continue

            else:

                dp = [[0] * (N + 1) for _ in range(word_len + 1)]

                braking = False

                for i in range(1, word_len + 1):

                    if braking:
                        break

                    for j in range(1, N + 1):

                        if word[i - 1] == s[j - 1]:
                            dp[i][j] = 1 + dp[i - 1][j - 1]
                        else:
                            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

                        if dp[i][j] == word_len:
                            substring_count += 1
                            braking = True
                            break

                    if dp[i][-1] == 0:
                        break

        return substring_count