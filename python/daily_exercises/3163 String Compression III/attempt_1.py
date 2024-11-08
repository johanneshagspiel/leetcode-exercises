class Solution():
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """

        comp = ""

        compare_char = ""
        count = 0

        for i in range(len(word)):
            if compare_char == "":
                compare_char = word[i]
                count += 1
            else:
                current_char = word[i]
                if current_char == compare_char:
                    if count == 9:
                        comp += str(count)
                        comp += compare_char
                        count = 1
                    else:
                        count += 1
                else:
                    comp += str(count)
                    comp += compare_char
                    count = 1

                compare_char = current_char

        comp += str(count)
        comp += compare_char
        return comp
