from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        fixed_array_list = [0 for letter in range(26)]
        for letter in p:
            letter_index = ord(letter) - 97
            fixed_array_list[letter_index] += 1

        result_list = []
        s_len = len(s)
        p_len = len(p)
        left_pointer = 0

        for right_pointer in range(s_len):
            right_char = s[right_pointer]
            right_char_index = ord(right_char) - 97

            fixed_array_list[right_char_index] -= 1

            while fixed_array_list[right_char_index] < 0:
                left_char = s[left_pointer]
                left_char_index = ord(left_char) - 97
                fixed_array_list[left_char_index] += 1
                left_pointer += 1

            distance_left_right = right_pointer - left_pointer
            if (distance_left_right == (p_len - 1)):
                result_list.append(left_pointer)

        return result_list

if __name__ == "__main__":
    solution = Solution()
    print(solution.findAnagrams("cbaebabacd", "abc"))
