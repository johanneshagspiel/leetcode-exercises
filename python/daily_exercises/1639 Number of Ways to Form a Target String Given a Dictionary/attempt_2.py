import collections


class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        max_word_length = len(words[0])
        max_target_length = len(target)

        mod_op = pow(10, 9) + 7

        index_char_dic = {}

        for word in words:
            for index, char in enumerate(word):

                if index not in index_char_dic:
                    index_char_dic[index] = {}
                if char not in index_char_dic[index]:
                    index_char_dic[index][char] = 0

                index_char_dic[index][char] += 1

        def rec_mem(index_target, index_word, mem_dic):

            if index_target >= max_target_length:
                return 1

            elif index_word >= max_word_length:
                return 0

            elif (index_target, index_word) in mem_dic:
                return mem_dic[(index_target, index_word)]

            else:

                cur_char = target[index_target]

                options = 0
                if cur_char in index_char_dic[index_word]:
                    char_count = index_char_dic[index_word][cur_char]

                    options += char_count * rec_mem(index_target + 1, index_word + 1, mem_dic)

                options += rec_mem(index_target, index_word + 1, mem_dic)

                mem_dic[(index_target, index_word)] = options

                return options

        res = rec_mem(0, 0, {})

        return res % mod_op
