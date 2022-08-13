from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        substring_count = 0
        N = len(s)
        seen_set = set()
        not_seen_set = set()

        for word in words:
            word_len = len(word)

            if word_len > N:
                continue

            else:

                if word in seen_set:
                    substring_count += 1
                    continue

                if word in not_seen_set:
                    continue

                word_position = 0
                string_position = 0

                while string_position < N:

                    if word[word_position] == s[string_position]:

                        word_position += 1
                        if word_position == word_len:
                            substring_count += 1
                            seen_set.add(word)
                            break

                    string_position += 1

                if word_position != word_len:
                    not_seen_set.add(word)

        return substring_count
