class Solution:
    def climbStairs(self, n: int) -> int:
        move_dic = {}
        return self.climbStairs_Helper(0, n, move_dic)

    def climbStairs_Helper(self, start_position, end_position, move_dic):
        if start_position > end_position:
            return 0
        if start_position == end_position:
            return 1
        if start_position in move_dic:
            return move_dic[start_position]
        move_dic[start_position] = self.climbStairs_Helper(start_position + 1, end_position, move_dic) + self.climbStairs_Helper(start_position + 2, end_position, move_dic)

        return move_dic[start_position]