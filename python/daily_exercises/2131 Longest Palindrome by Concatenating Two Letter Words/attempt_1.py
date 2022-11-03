class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        word_count = collections.Counter(words)
        word_len = 0
        self_palindrome = False

        for word in words:
            current_count = word_count[word]
            reverse_word = word[::-1]

            if current_count > 0:

                if reverse_word in word_count:

                    reverse_count = word_count[reverse_word]

                    if reverse_count > 0:

                        if current_count == 1 and word[0] == word[1]:
                            if not self_palindrome:
                                word_len += 2
                                word_count[word] -= 1
                                self_palindrome = True
                        else:
                            word_len += 4
                            word_count[word] -= 1
                            word_count[reverse_word] -= 1

        return word_len
