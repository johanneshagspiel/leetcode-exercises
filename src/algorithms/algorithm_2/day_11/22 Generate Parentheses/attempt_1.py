from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return []

        result_list = []

        def back_track(open_parentheses, close_parentheses, current_list):
            if open_parentheses == n and close_parentheses == n:
                result_list.append("".join(current_list))
                return
            elif open_parentheses > n:
                return
            elif close_parentheses > n:
                return
            else:
                if open_parentheses == close_parentheses:
                    current_list.append("(")
                    back_track(open_parentheses + 1, close_parentheses, current_list)
                    current_list.pop()
                elif open_parentheses > close_parentheses:

                    if open_parentheses < n:
                        current_list.append("(")
                        back_track(open_parentheses + 1, close_parentheses, current_list)
                        current_list.pop()

                    current_list.append(")")
                    back_track(open_parentheses, close_parentheses + 1, current_list)
                    current_list.pop()

        back_track(0, 0, [])
        return result_list

