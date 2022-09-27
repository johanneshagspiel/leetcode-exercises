class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        n = len(dominoes)

        left_to_right = list(dominoes)
        right_to_left = list(dominoes)

        pushed_left = False
        for position in range(n-1, -1, -1):
            if pushed_left:
                if dominoes[position] == ".":
                    left_to_right[position] = "L"
                else:
                    pushed_left = False
            else:
                if dominoes[position] == "L":
                    pushed_left = True

        pushed_right = False
        for position in range(n):
            if pushed_right:
                if dominoes[position] == ".":
                    right_to_left[position] = "R"
                else:
                    pushed_right = False
            else:
                if dominoes[position] == "R":
                    pushed_right = True


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
                elif left == "L" and right == ".":
                    res += left
                elif left == "." and right == "R":
                    res += right
                else:
                    res += right

        return res
