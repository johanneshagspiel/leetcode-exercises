from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        heads = [[] for _ in range(26)]
        substring_count = 0

        for word in words:
            iterr = iter(word[1:])

            insert_position = ord(word[0]) - ord('a')
            heads[insert_position].append(iterr)

        for char in s:
            letter_index = ord(char) - ord('a')
            bucket = heads[letter_index]
            heads[letter_index] = []

            while bucket:
                iterr = bucket.pop()

                nxt = next(iterr, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(iterr)
                else:
                    substring_count += 1

        return substring_count
