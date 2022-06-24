class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairs_Helper(0, n, {})

    def climbStairs_Helper(self, start_position, end_position, move_dic):
        if start_position > end_position:
            return 0
        elif start_position == end_position:
            return 1
        elif start_position in move_dic:
            return move_dic[start_position]
        else:
            moves = self.climbStairs_Helper(start_position + 1, end_position, move_dic) + self.climbStairs_Helper(start_position + 2, end_position, move_dic)
            move_dic[start_position] = moves
            return moves
