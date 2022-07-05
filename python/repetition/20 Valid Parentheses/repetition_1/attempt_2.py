class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {'(': ')', '[': ']', '{': '}'}
        open = {'(', '[', '{'}
        open_parenthesis = []

        for char in s:
            if char in open:
                open_parenthesis.append(char)
            else:
                if len(open_parenthesis) == 0:
                    return False
                else:
                    last_open = open_parenthesis.pop()

                    if mapping[last_open] != char:
                        return False

        return len(open_parenthesis) == 0