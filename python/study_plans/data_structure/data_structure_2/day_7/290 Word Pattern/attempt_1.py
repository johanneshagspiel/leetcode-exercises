class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        word_list = s.split(" ")
        pattern_list = list(pattern)

        if len(word_list) != len(pattern_list):
            return False

        pattern_counter = {}
        seen_set = set()

        word_counter = 0

        for cur_patter in pattern_list:

            cur_word = word_list[word_counter]

            if cur_patter in pattern_counter:
                word = pattern_counter[cur_patter]
                if word != cur_word:
                    return False
            else:
                if cur_word in seen_set:
                    return False

                else:
                    pattern_counter[cur_patter] = cur_word
                    seen_set.add(cur_word)

            word_counter += 1

        return True
