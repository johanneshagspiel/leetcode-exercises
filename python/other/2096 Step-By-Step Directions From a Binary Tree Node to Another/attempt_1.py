# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        if not root:
            return ""

        stack = []

        if root.left:
            stack.append((root.left, "L"))
        if root.right:
            stack.append((root.right, "R"))

        start_moves = ""
        dest_moves = ""

        while stack:

            node, move_string = stack.pop()

            if node.val == startValue:
                start_moves = move_string

            elif node.val == destValue:
                dest_moves = move_string

            else:
                if node.left:
                    stack.append((node.left, move_string + "L"))
                if node.right:
                    stack.append((node.right, move_string + "R"))

        star_moves_len = len(start_moves)
        dest_moves_len = len(dest_moves)

        cleaned_star_moves_count = 0

        star_pointer = 0
        dest_pointer = 0

        while star_pointer < star_moves_len and dest_pointer < dest_moves_len and start_moves[star_pointer] == dest_moves[dest_pointer]:
            cleaned_star_moves_count += 1
            star_pointer += 1
            dest_pointer += 1

        res_dest_moves = dest_moves[cleaned_star_moves_count:]

        if len(res_dest_moves) == 0:
            return start_moves[cleaned_star_moves_count:]

        else:
            res_star_moves = ""
            for move in range(star_moves_len - cleaned_star_moves_count):
                res_star_moves += "U"

            return res_star_moves + res_dest_moves
