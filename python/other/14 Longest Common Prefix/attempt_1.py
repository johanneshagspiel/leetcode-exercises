from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = []

        first_list = strs[0]
        other_lists = strs[1:]

        position = 0
        keep_going = True

        while keep_going:

            if position >= len(first_list):
                keep_going = False
                break

            candidate = first_list[position]

            for other_list in other_lists:
                if position >= len(other_list):
                    keep_going = False
                    break
                elif other_list[position] != candidate:
                    keep_going = False
                    break

            if keep_going:
                prefix.append(candidate)
                position += 1

        return "".join(prefix)
