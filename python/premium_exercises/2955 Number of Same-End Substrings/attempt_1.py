class Solution(object):
    def sameEndSubstringCount(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        string_length = len(s)
        left_to_right_char_count_matrix = [[0 for i in range(26)] for char in range(string_length)]

        for i in range(string_length):
            current_char = s[i]
            current_char_index = ord(current_char) - 97

            previous_index = max(0, i - 1)
            previous_char_count_list = left_to_right_char_count_matrix[previous_index]
            current_char_count_list = left_to_right_char_count_matrix[i]

            for char_index in range(26):
                if char_index == current_char_index:
                    current_char_count_list[char_index] = previous_char_count_list[char_index] + 1
                else:
                    current_char_count_list[char_index] = previous_char_count_list[char_index]

            left_to_right_char_count_matrix[i] = current_char_count_list

        res = []

        for query in queries:
            curr_count = 0
            for char_index in range(26):
                end_index = query[1]
                start_index = query[0] - 1

                end_count = left_to_right_char_count_matrix[end_index][char_index]
                start_count = 0
                if start_index >= 0:
                    start_count = left_to_right_char_count_matrix[start_index][char_index]

                count = end_count - start_count

                to_add = (count * (count + 1)) / 2
                curr_count += to_add

            res.append(curr_count)

        return res
