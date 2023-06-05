class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        n = len(s) - 1
        n_decodings = 1

        while n > 0:

            number = s[n]
            previous_number = s[n-1]

            if number == '0':
                if previous_number == '2' or previous_number == '1':
                    n -= 2
                else:
                    return 0
            else:
                if previous_number == '1':
                    n_decodings += 1
                elif previous_number == '2':
                    int_number = int(number)
                    if int_number <= 6:
                        n_decodings += 1
                n -= 1

        return n_decodings
    