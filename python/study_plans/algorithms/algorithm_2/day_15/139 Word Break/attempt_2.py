from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        self.result = False
        n = len(s)

        def rec(start_index):

            if start_index == n:
                self.result = True

            else:

                for end_index in range(n, -1, -1):
                    sub_string = s[start_index:(end_index+1)]

                    if sub_string in wordDict:
                        rec(end_index + 1)

        rec(0)
        return self.result

