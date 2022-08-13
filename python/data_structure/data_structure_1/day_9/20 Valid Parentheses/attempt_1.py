import collections


class Solution:
    def isValid(self, s: str) -> bool:
        open_parentheses_stack = []
        combination_dic = {"(" : ")", "{" : "}", "[" : "]"}

        for char in s:
            if char == "(" or char == "{" or char == "[":
                open_parentheses_stack.append(char)
            elif char == ")" or char == "}" or char == "]":
                if len(open_parentheses_stack) == 0:
                    return False
                else:
                    latest_open_char = open_parentheses_stack.pop()
                    if combination_dic[latest_open_char] != char:
                        return False
            else:
                return False

        return len(open_parentheses_stack) == 0
