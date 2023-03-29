class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        num_dishes = len(satisfaction)

        satisfaction.sort()
        def rec_mem(dish_num, prev_used, mem_dic):

            if dish_num >= num_dishes:
                return 0
            elif (dish_num, prev_used) in mem_dic:
                return mem_dic[(dish_num, prev_used)]
            else:
                without_res = rec_mem(dish_num + 1, prev_used, mem_dic)
                with_res = prev_used * satisfaction[dish_num] + rec_mem(dish_num + 1, prev_used + 1, mem_dic)

                mem_dic[(dish_num, prev_used)] = max(without_res, with_res)
                return mem_dic[(dish_num, prev_used)]

        return rec_mem(0, 1, {})