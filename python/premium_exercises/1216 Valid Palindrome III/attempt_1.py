class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        def is_valid_palindrome(i, j, s, memo):

            if i == j:
                return 0

            elif i == j - 1:
                return 1 if s[i] != s[j] else 0

            elif memo[i][j] != -1:
                return memo[i][j]

            else:
                if s[i] == s[j]:
                    memo[i][j] = is_valid_palindrome(i + 1, j - 1, s, memo)
                    return memo[i][j]
                else:
                    memo[i][j] = 1 + min(is_valid_palindrome(i + 1, j, s, memo), is_valid_palindrome(i, j - 1, s, memo))
                    return memo[i][j]

        memo = [[-1] * (len(s)) for _ in range(len(s))]
        is_valid_palindrome(0, len(s) - 1, s, memo)
        return memo[0][- 1] <= k
