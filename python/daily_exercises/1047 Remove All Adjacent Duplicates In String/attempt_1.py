class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for char in s:

            if stack:
                if stack[-1] == char:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return "".join(stack)