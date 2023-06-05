class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        
        num_decodings = 1
        n = len(s)
        skip_next = False

        for index in range(n - 1):
            number = s[index]
            next_number_int = int(s[index + 1])

            if skip_next:
                skip_next = False
            else:

                if number == '0':
                    return 0

                elif number == '1':
                    if next_number_int == 0:
                        skip_next = True
                    else:
                        num_decodings += 1

                elif number == '2':
                    if next_number_int <= 6:
                        if next_number_int == 0:
                            skip_next = True
                        else:
                            num_decodings += 1

        return num_decodings
