class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        def rec_push(dominoes):

            n = len(dominoes)

            left_to_right = list(dominoes)
            right_to_left = list(dominoes)

            for position in range(n):
                if position > 0:
                    if dominoes[position] == "L":
                        left_to_right[position - 1] = "L"


                if position < (n - 1):
                    if dominoes[position] == "R":
                        right_to_left[position + 1] = "R"

            res = ""

            for position in range(n):
                original = dominoes[position]
                left = left_to_right[position]
                right = right_to_left[position]

                if original != ".":
                    res += original
                else:
                    if left == "L" and right == "R":
                        res += original
                    elif left == "L":
                        res += left
                    else:
                        res += right

            for position in range(n):
                original = dominoes[position]
                new = res[position]

                if original != new:
                    return True, res

            return False, res


        keep_going = True

        while keep_going:
            changed, dominoes = rec_push(dominoes)
            keep_going = changed

        return dominoes