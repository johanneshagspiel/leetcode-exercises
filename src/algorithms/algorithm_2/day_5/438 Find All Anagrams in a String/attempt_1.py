import copy
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        fixed_array_list = [0 for letter in range(26)]
        hitcount = len(p)

        result_list = []

        s_len = len(s)

        for letter in p:
            letter_index = ord(letter) - 97
            fixed_array_list[letter_index] += 1

        for start_index in range(s_len - hitcount):
            temp_array = copy.deepcopy(fixed_array_list)
            temp_hitcount = copy.deepcopy(hitcount)
            temp_index = start_index

            while temp_index < s_len:
                s_char = s[temp_index]
                s_char_index = ord(s_char) - 97

                if temp_array[s_char_index] > 0:
                    temp_array[s_char_index] -= 1
                    temp_hitcount -= 1
                    temp_index += 1

                    if temp_hitcount == 0:
                        result_list.append(start_index)
                        break
                else:
                    break

        return result_list

if __name__ == "__main__":
    solution = Solution()
    print(solution.findAnagrams("cbaebabacd", "abc"))