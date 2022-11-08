class Solution:
    def makeGood(self, s: str) -> str:

        input_s = s

        while True:

            no_change = True
            skip_index = False

            skip_set = set()

            len_string = len(input_s)

            for i in range(0, len_string - 1):

                if skip_index:
                    skip_index = False

                else:
                    char_1 = input_s[i]
                    char_2 = input_s[i + 1]

                    if char_1.islower() and char_2.isupper():
                        comp_1 = char_1
                        comp_2 = char_2.lower()

                        if comp_1 == comp_2:
                            skip_set.add(i)
                            skip_set.add(i + 1)
                            no_change = False
                            skip_index = True

                    elif char_1.isupper() and char_2.islower():
                        comp_1 = char_1.lower()
                        comp_2 = char_2

                        if comp_1 == comp_2:
                            skip_set.add(i)
                            skip_set.add(i + 1)
                            no_change = False
                            skip_index = True

            if no_change:
                return input_s
            else:
                temp_string = ""
                for i in range(len_string):
                    if i not in skip_set:
                        temp_string += input_s[i]

                input_s = temp_string

