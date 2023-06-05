class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while True:
            key = str(n)
            if key in seen:
                if key == '1':
                    return True
                else:
                    return False
            else:
                seen.add(key)
                int_list = [int(x) for x in list(str(n))]
                n = str(sum([str(pow(x, 2)) for x in int_list]))
