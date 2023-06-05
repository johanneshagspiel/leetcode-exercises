from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result_list = []

        def back_track(open, closed, current_list):

            if open == n and closed == n:
                result_list.append("".join(current_list))

            elif closed > open:
                return

            elif open > n:
                return

            elif closed > n:
                return

            else:
                current_list.append('(')
                back_track(open+1, closed, current_list)
                current_list.pop()

                current_list.append(')')
                back_track(open, closed+1, current_list)
                current_list.pop()

        back_track(0, 0, [])
        return result_list
