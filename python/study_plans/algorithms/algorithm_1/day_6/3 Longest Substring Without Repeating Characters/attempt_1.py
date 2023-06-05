class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_list = list(s)
        string_length = len(s)
        longest_substring = 0

        for start_index in range(string_length):

            start_char = char_list[start_index]
            end_index = start_index + 1

            while (end_index < string_length):

                end_char = char_list[end_index]

                if (start_char != end_char):
                    end_index += 1
                else:
                    end_index = st

            sub_string_length = end_index - start_index
            if sub_string_length > longest_substring:
                longest_substring = sub_string_length

        return longest_substring


if __name__ == '__main__':
    solution = Solution()
    s = "abcabcbb"
    output = solution.lengthOfLongestSubstring(s)
    print(output)