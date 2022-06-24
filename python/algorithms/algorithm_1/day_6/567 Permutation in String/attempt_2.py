class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_list = list(s1)
        s2_list = list(s2)

        if len(s1) > len(s2):
            return False

        s1_array = [0]*26

        for char in s1_list:
            index = ord(char) - 97
            s1_array[index] += 1

        for start_index in range(0, (len(s2_list) - len(s1_list)) + 1):
            s2_array = [0]*26

            for end_index in range(len(s1_list)):
                char_2 = s2_list[start_index + end_index]
                s2_array[ord(char_2) - 97] += 1

            if self.matches(s1_array, s2_array):
                return True

        return False

    def matches(self, array_1, array_2):
        for index in range(len(array_1)):
            if array_1[index] != array_2[index]:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    s1 = "adc"
    s2 = "dcda"
    output = solution.checkInclusion(s1, s2)
    print(output)