from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        ans = [[]]

        for char in s:

            N = len(ans)
            if char.isalpha():
                for i in range(N):
                    ans.append(ans[i][::])
                    ans[i].append(char.lower())
                    ans[i+N].append(char.upper())

            else:
                for i in range(N):
                    ans[i].append(char)

        return ans
