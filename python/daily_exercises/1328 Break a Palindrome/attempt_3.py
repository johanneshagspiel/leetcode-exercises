class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)

        if n <= 1:
            return ""

        char_list = list(palindrome)

        for i in range(n // 2):
            if char_list[i] != "a":
                char_list[i] = "a"
                return "".join(char_list)

        char_list[-1] = "b"
        return "".join(char_list)
