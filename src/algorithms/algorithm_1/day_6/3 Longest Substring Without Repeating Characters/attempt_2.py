class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fixed_array = [0]*26
        s_list = list(s)

        left = right = 0
        max_sub_string_length = 0

        while right < len(s):
            r_char = s_list[right]
            r_index = ord(r_char) - 97
            fixed_array[r_index] += 1

            while fixed_array[r_index] > 1:
                left_char = s_list[left]
                l_index = ord(left_char) - 97
                fixed_array[l_index] -= 1
                left += 1

            right += 1

            max_sub_string_length = max(max_sub_string_length, right - left + 1)

        return max_sub_string_length


if __name__ == '__main__':
    solution = Solution()
    s = "abcabcbb"
    output = solution.lengthOfLongestSubstring(s)
    print(output)