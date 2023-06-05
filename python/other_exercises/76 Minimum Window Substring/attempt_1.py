import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freq_counter = collections.Counter(t)
        to_find_characters = len(freq_counter.keys())

        left = 0
        right = 0

        min_len = float("inf")
        solution = ""

        first_time = True

        for char in s:

            if char in freq_counter:

                if freq_counter[char] != 0:
                    freq_counter[char] -= 1

                    if freq_counter[char] == 0:
                        to_find_characters -= 1

                else:

                    char_not_found = True

                    while char_not_found:

                        left_char = s[left]
                        if left_char in freq_counter:

                            if left_char == char:
                                char_not_found = False
                            else:
                                freq_counter[left_char] += 1
                                if freq_counter[left_char] > 0:
                                    to_find_characters += 1
                        left += 1

                    other_char_not_found = True

                    while other_char_not_found and left < right:

                        left_char = s[left]
                        if left_char in freq_counter:
                            other_char_not_found = False
                        else:
                            left += 1

            right += 1

            if to_find_characters == 0:

                if first_time:

                    while s[left] not in freq_counter:
                        left += 1
                    first_time = False

                if (right - left) < min_len:
                    min_len = right - left
                    solution = s[left:right]

                while to_find_characters == 0:

                    left_char = s[left]
                    if left_char in freq_counter:
                        freq_counter[left_char] += 1
                        if freq_counter[left_char] > 0:
                            to_find_characters += 1

                    left += 1

                other_char_not_found = True

                while other_char_not_found and left < right:

                    left_char = s[left]
                    if left_char in freq_counter:
                        other_char_not_found = False
                    else:
                        left += 1

        return solution if min_len != float("inf") else ""
