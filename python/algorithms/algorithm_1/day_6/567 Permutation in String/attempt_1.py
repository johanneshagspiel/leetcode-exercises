import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_counter = collections.Counter(s1)
        needed_zero_hits = len(s1_counter.keys())

        s2_list = list(s2)
        s2_list_length = len(s2_list)

        s2_counter_dic = {}
        s2_zero_hits = 0
        left_pointer = 0

        for start_index in range(s2_list_length):

            current_char = s2_list[start_index]
            if current_char in s2_counter_dic:
                s2_counter_dic[current_char] -= 1

                if s2_counter_dic[current_char] == 0:
                    s2_zero_hits += 1

                    if s2_zero_hits == needed_zero_hits:
                        return True

                if s2_counter_dic[current_char] < 0:

                    char_at_left_pointer = s2_list[left_pointer]
                    if char_at_left_pointer == current_char:
                        s2_counter_dic[current_char] += 1
                        left_pointer += 1
                    else:
                        s2_counter_dic = {}
                        s2_zero_hits = 0
            else:
                if current_char in s1_counter:
                    needed_amount = s1_counter[current_char]
                    new_amount = needed_amount - 1
                    s2_counter_dic[current_char] = new_amount

                    if new_amount == 0:
                        s2_zero_hits += 1

                        if s2_zero_hits == needed_zero_hits:
                            return True

                else:
                    s2_counter_dic = {}
                    s2_zero_hits = 0

        return False

if __name__ == '__main__':
    solution = Solution()
    s1 = "adc"
    s2 = "dcda"
    output = solution.checkInclusion(s1, s2)
    print(output)