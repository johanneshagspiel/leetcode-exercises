import collections


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        forget_dic = collections.Counter({forget: 1})
        delay_dic = collections.Counter({delay: 1})
        sharing = 0
        aware = 1

        for day in range(1, n):
            sharing += delay_dic[day] - forget_dic[day]
            aware += sharing - forget_dic[day]

            forget_dic[day+forget] = sharing
            delay_dic[day+delay] = sharing

        return aware % (pow(10, 9) + 7)
