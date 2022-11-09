class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        for char in s:

            if stack:
                if abs(ord(stack[-1]) - ord(char)) == 32:
                    stack.pop()
                else:
                    stack.append(char)

            else:
                stack.append(char)

        return "".join(stack)
