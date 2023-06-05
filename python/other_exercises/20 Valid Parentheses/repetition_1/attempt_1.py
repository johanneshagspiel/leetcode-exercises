class Solution:
    def isValid(self, s: str) -> bool:

        open_set = {'(', '[', '{'}
        correspondence = {'(': ')', '[': ']', '{': '}'}
        to_be_closed = []

        for char in s:
            if char in open_set:
                to_be_closed.append(char)
            else:
                if len(to_be_closed) == 0:
                    return False
                else:
                    latest_to_be_closed = to_be_closed.pop()
                    if correspondence[latest_to_be_closed] != char:
                        return False

        if len(to_be_closed) > 0:
            return False
        else:
            return True
