class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")
        number_words = len(word_list)

        for index in range(0, number_words):

            word = word_list[index]

            split_word = list(word)
            split_word[:] = split_word[::-1]
            new_word = "".join(split_word)

            word_list[index] = new_word

        word_list = " ".join(word_list)

        return word_list


if __name__ == '__main__':

    solution = Solution()
    s = "Let's take LeetCode contest"
    solution.reverseWords(s)