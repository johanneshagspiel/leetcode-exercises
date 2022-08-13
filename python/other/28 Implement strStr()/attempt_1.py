class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n_len = len(needle)
        h_len = len(haystack)

        if n_len == 0:
            return 0

        found_index = -1

        if h_len < n_len:
            return found_index
        elif h_len == n_len:
            if haystack == needle:
                return 0
            else:
                return -1

        n_position = 0

        for h_position in range(h_len - n_len):

            if haystack[h_position] == needle[n_position]:

                if found_index == -1:
                    found_index = h_position

                n_position += 1
            else:
                found_index = -1
                n_position = 0

            if n_position == n_len:
                return found_index

        return found_index

