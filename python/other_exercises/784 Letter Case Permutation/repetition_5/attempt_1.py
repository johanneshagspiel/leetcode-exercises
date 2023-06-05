class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:


        ans = [[]]

        for letter in s:

            N = len(ans)

            if letter.isalpha():
                for i in range(N):
                    ans.append(ans[i][::])
                    ans[i].append(letter.lower())
                    ans[N+i].append(letter.upper())

            else:
                for i in range(N):
                    ans[i].append(letter)


        return map(lambda x: "".join(x), ans)

