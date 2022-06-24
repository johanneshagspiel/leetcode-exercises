from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key= lambda x: len(x), reverse=True)
        longest_chain = 1
        n = len(words)


        def one_difference(start_word, compare_word):

            for index in range(len(start_word)):
                test_word = start_word[:index] + start_word[(index+1):]
                if test_word == compare_word:
                    return True
            return False


        for start_index in range(n):
            current_word = words[start_index]
            current_chain = 1

            for end_index in range(start_index+1, n):
                next_word = words[end_index]

                if len(next_word) == len(current_word):
                    continue
                elif len(next_word) < len(current_word) - 1:
                    break
                else:
                    if one_difference(current_word, next_word):
                        current_chain += 1
                        current_word = next_word

            longest_chain = max(longest_chain, current_chain)

        return longest_chain