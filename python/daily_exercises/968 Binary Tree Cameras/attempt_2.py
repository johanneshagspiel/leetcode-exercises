import math


class Solution(object):
    def minCameraCover(self, root):
        def solve(node):
            if not node:
                return 0, 0, math.inf
            else:
                left = solve(node.left)
                right = solve(node.right)

                case_0 = left[1] + right[1]
                case_1 = min(left[2] + min(right[1:]), right[2] + min(left[1:]))
                case_2 = 1 + min(left) + min(right)

                return case_0, case_1, case_2

        return min(solve(root)[1:])