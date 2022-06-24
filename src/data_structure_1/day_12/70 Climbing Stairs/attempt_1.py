class Solution:
    def climbStairs(self, n: int) -> int:

        def climber_helper(start_point, end_point, move_dic):

            if start_point > end_point:
                return 0
            elif start_point == end_point:
                return 1
            elif start_point in move_dic:
                return move_dic[start_point]
            else:
                new_entry = climber_helper(start_point + 1, end_point, move_dic) + climber_helper(start_point + 2, end_point, move_dic)
                move_dic[new_entry]
                return new_entry

        return climber_helper(0, n, {})
