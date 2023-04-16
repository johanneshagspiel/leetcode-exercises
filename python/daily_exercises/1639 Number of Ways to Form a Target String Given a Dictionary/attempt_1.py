class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        max_word_length = len(words[0])
        max_target_length = len(target)

        mod_op = pow(10, 9) + 7

        def rec_mem(index_target, index_word, mem_dic):

            if index_target >= max_target_length:
                return 1

            elif index_word >= max_word_length:
                return 0

            elif (index_target, index_word) in mem_dic:
                return mem_dic[(index_target, index_word)]

            else:

                options = 0

                for word in words:
                    if word[index_word] == target[index_target]:
                        options += rec_mem(index_target + 1, index_word + 1, mem_dic)

                options += rec_mem(index_target, index_word + 1, mem_dic)

                mem_dic[(index_target, index_word)] = options % mod_op

                return options

        return rec_mem(0, 0, {})
