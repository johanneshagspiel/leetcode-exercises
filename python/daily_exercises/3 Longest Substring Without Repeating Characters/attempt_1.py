class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        fixed_array = [0 for number in range(26)]

        left_pointer = 0
        right_pointer = 0
        max_len = 0

        for char in s:
            array_index = ord(char) - 97
            occurences = fixed_array[array_index]
            right_pointer += 1
            fixed_array[array_index] += 1

            if occurences == 0:
                temp_len = right_pointer - left_pointer
                if temp_len > max_len:
                    max_len = temp_len

            else:

                while fixed_array[array_index] > 1:
                    char_at_left_pointer = s[left_pointer]
                    left_pointer_array_index = ord(char_at_left_pointer) - 97
                    fixed_array[left_pointer_array_index] -= 1
                    left_pointer += 1

        return max_len



if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkew"))



