class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_list = list(s1)
        s2_list = list(s2)

        s1_length = len(s1_list)
        s2_length = len(s2_list)

        if s1_length > s2_length:
            return False

        s1_array = [0]*26
        s2_array = [0]*26

        for index in range(s1_length):
            char_1 = s1_list[index]
            char_1_array_index = ord(char_1) - 97
            s1_array[char_1_array_index] += 1

            char_2 = s2_list[index]
            char_2_array_index = ord(char_2) - 97
            s2_array[char_2_array_index] += 1


        for start_index in range(0, s2_length - s1_length):

            if self.matches(s1_array, s2_array):
                return True

            increase_char = s2_list[s1_length + start_index]
            increase_char_index = ord(increase_char) - 97
            s2_array[increase_char_index] += 1

            decrease_char = s2_list[start_index]
            decrease_char_index = ord(decrease_char) - 97
            s2_array[decrease_char_index] -= 1

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