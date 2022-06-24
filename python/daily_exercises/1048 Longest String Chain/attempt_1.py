from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(reverse=True, key= lambda x: len(x))
        max_string_chain = 0

        for start_index in range(len(words)):
            start_word = words[start_index]
            string_chain = 0
            redo = False

            for compare_index in range(start_index, len(words)):
                compare_word = words[compare_index]

                if len(start_word) == len(compare_word):
                    continue
                elif len(start_word) == (len(compare_word) + 1):
                    one_off = self.difference_by_one(start_word, compare_word)

                    if one_off:
                        string_chain += 1
                        start_word = compare_word
                        redo = False
                    else:
                        redo = True
                else:
                    break

            if string_chain > max_string_chain:
                max_string_chain = string_chain

        return max_string_chain

    def difference_by_one(self, start_word, compare_word):

        for pop_index in range(len(start_word)):
            temp_word = start_word
            temp_word = temp_word[:pop_index] + temp_word[pop_index+1:]
            if temp_word == compare_word:
                return True

        return False

if __name__ == "__main__":
    solution = Solution()
    solution.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"])