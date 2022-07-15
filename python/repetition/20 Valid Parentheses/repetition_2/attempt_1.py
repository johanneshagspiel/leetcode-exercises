class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {'(': ')', '{': '}', '[': ']'}

        open_list = []

        for char in s:
            if char in ('(', '[', '{'):
                open_list.append(char)
            else:
                if len(open_list) == 0:
                    return False
                else:
                    last_open = open_list.pop()

                    if mapping[last_open] != char:
                        return False

        return len(open_list) == 0
