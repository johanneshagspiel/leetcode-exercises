from typing import List

class Solution:

    def maxProduct(self, words: List[str]) -> int:

        length_words = len(words)
        max_length = 0

        for start_index in range(0, length_words):
            first_word = words[start_index]
            first_word_set = set(list(first_word))

            for end_index in range(start_index + 1, length_words):
                second_word = words[end_index]
                second_word_set = set(list(second_word))

                intersection = first_word_set.intersection(second_word_set)

                if len(intersection) == 0:
                    combined_length = len(first_word) * len(second_word)

                    if combined_length > max_length:
                        max_length = combined_length

        return max_length

if __name__ == '__main__':
    solution = Solution()

    input_1 = ["abcw","baz","foo","bar","xtfn","abcdef"]
    output_1 = solution.maxProduct(input_1)
    expected_1 = 16

    print(output_1)