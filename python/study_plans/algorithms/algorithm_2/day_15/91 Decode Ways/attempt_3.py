class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        n = len(s)
        self.n_decodings = 1

        def rec(start_index):

            if start_index < n-1:
                number = s[start_index]
                next_number = int(s[start_index + 1])

                if number == '0':
                    return 0

                elif number == '1':
                    if next_number == 0:
                        rec(start_index + 2)
                    else:
                        self.n_decodings += 1
                        rec(start_index + 1)
                        rec(start_index + 2)

                elif number == '2':
                    if next_number == 0:
                        rec(start_index + 2)
                    elif next_number <= 6:
                        self.n_decodings += 1
                        rec(start_index + 1)
                        rec(start_index + 2)
                    else:
                        rec(start_index + 1)

                else:
                    rec(start_index + 1)

        rec(0)
        return self.n_decodings


