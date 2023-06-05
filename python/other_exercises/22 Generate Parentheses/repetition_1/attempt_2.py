from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result_list = []

        def back_track(open_remaining, closed_remaining, current_list):

            if (open_remaining == 0) and (closed_remaining == 0):
                key = "".join(current_list)
                result_list.append(key)

            elif open_remaining < 0:
                return

            elif closed_remaining < 0:
                return

            elif closed_remaining < open_remaining:
                return

            else:
                current_list.append("(")
                back_track(open_remaining-1, closed_remaining, current_list)
                current_list.pop()

                current_list.append(")")
                back_track(open_remaining, closed_remaining-1, current_list)
                current_list.pop()

        back_track(n, n, [])
        return result_list
