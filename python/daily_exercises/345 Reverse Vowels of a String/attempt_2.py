class Solution:
    def reverseVowels(self, s: str) -> str:
        str_list = list(s)
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        start = 0
        end = len(str_list) - 1

        while start < end:

            if str_list[start] in vowel_list and str_list[end] in vowel_list:
                str_list[start], str_list[end] = str_list[end], str_list[start]
                start += 1
                end -= 1

            elif str_list[start] not in vowel_list:
                start += 1

            else:
                end -= 1

        return "".join(str_list)
