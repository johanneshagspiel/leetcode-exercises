from typing import List
from collections import OrderedDict

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for num in range(1, n + 1):

            fizz_buzz_dic = OrderedDict({3: "Fizz", 5: "Buzz"})

            res = ""

            for key in fizz_buzz_dic.keys():
                if num % key == 0:
                    res += fizz_buzz_dic[key]

            if not res:
                res = str(num)

            ans.append(res)

        return ans
