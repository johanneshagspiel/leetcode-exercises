class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        for i in range(len(s)):

            current_char = s[i]

            if stack:
                if (abs(ord(stack[-1]) - ord(current_char)) == 32):
                    stack.pop()
                else:
                    stack.append(current_char)
            else:
                stack.append(current_char)

        return "".join(stack)
