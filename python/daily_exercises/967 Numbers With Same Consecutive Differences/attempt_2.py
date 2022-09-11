from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        res = []

        def back_track(num_list):

            if len(num_list) == n:
                string = "".join([str(x) for x in num_list])
                res.append(string)

            elif len(num_list) > n:
                return

            else:

                last_number = num_list[-1]

                if k == 0:
                    num_list.append(last_number)
                    back_track(num_list)

                else:
                    inc = last_number + k
                    dec = last_number - k

                    if inc <= 9:
                        num_list.append(inc)
                        back_track(num_list)
                        num_list.pop()


                    if dec >= 0:
                        num_list.append(dec)
                        back_track(num_list)
                        num_list.pop()


        for num in range(1, 10):
            back_track([num])

        return res

