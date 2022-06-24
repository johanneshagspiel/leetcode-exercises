class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_list = list(s1)
        s2_list = list(s2)

        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        s1_array = [0] * 26
        s2_array = [0] * 26

        for index in range(s1_len):
            char_index_1 = ord(s1_list[index]) - 97
            s1_array[char_index_1] += 1

            char_index_2 = ord(s2_list[index]) - 97
            s2_array[char_index_2] += 1

        for index in range(0, s2_len - s1_len):

            if self.matches(s1_array, s2_array):
                return True

            char_index_1 = ord(s2_list[index + s1_len]) - 97
            s2_array[char_index_1] += 1

            char_index_2 = ord(s2_list[index]) - 97
            s2_array[char_index_2] -= 1

        return self.matches(s1_array, s2_array)

    def matches(self, array_1, array_2):

        for index in range(26):
            value_1 = array_1[index]
            value_2 = array_2[index]

            if value_1 != value_2:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    s1 = "adc"
    s2 = "dcda"
    output = solution.checkInclusion(s1, s2)
    print(output)